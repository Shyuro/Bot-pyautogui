import pyautogui
import random
import os
import sys
from pyHM import mouse
import time
import datetime


def resource_path0(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    base_path = getattr(
        sys,
        '_MEIPASS',
        os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)


class logging:
    @staticmethod
    def debug(msg):
        time.sleep(0.5)
        print(f'>> '
              f'{datetime.datetime.today().hour}:{datetime.datetime.today().minute}:{datetime.datetime.today().second}'
              f' DEBUG: {msg}')


class Program:

    lista_botoes = [
        (411, 524, 114, 29), (843, 524, 114, 29), (1274, 524, 114, 29), (1706, 524, 114, 29),
        (411, 823, 114, 29), (843, 823, 114, 29), (1274, 823, 114, 29), (1706, 823, 114, 29)
    ]

    solicitado = resource_path0('img/solicitado.png')
    ganharmoedas = resource_path0('img/ganharmoedas.bmp')
    confirmarimg = resource_path0('img/confirmar.png')
    atualizarimg = resource_path0('img/atualizar.png')
    curtiroff = resource_path0('img/curtiroff.png')
    curtiron = resource_path0('img/curtiron.png')
    indisponivel = resource_path0('img/indisponivel.png')
    seguindo = resource_path0('img/seguindo.png')
    seguir = resource_path0('img/seguir.png')
    xpag = resource_path0('img/xpag.png')
    xinstelikes = resource_path0('img/xinstelikes.png')
    indisponivel2 = resource_path0('img/indisponivel2.png')

    def __init__(self, modo):

        self.count = 0  # numero de trades finalizadas
        self.testes = 0  # faz 20 testes e se não encontrar finaliza
        self.update = random.randint(3, 8)
        self.modo = modo
        self.tentativa = 0
        self.finalizar = 0

        logging.debug('Aperte Esc para sair!!')
        try:
            logging.debug('iniciando programa...')
            while True:
                if self.finalizar >= 6:
                    logging.debug('Botões não foram encontrados!')
                    logging.debug('Tente Novamente!')
                    break
                if self.count >= self.update:
                    Program.atualizar(self)
                Program.b_ganharmoedas(self)
                if modo == 'seguir':
                    Program.b_seguir(self)
                elif modo == 'curtir':
                    Program.b_curtir(self)
                Program.confirmar(self)
        except KeyboardInterrupt:
            logging.debug('finalizando programa...')
            sys.exit()

    def b_ganharmoedas(self):
        logging.debug('Botão ganhar moedas')
        logging.debug('Detectando botão')
        while True:

            regiao = random.choice(self.lista_botoes)
            ganharmoedas = pyautogui.locateOnScreen(Program.ganharmoedas, confidence=0.9, region=regiao)
            if ganharmoedas:
                logging.debug('Botão detectado!')
                try:
                    x, y = pyautogui.locateCenterOnScreen(Program.ganharmoedas,
                                                          confidence=0.9,
                                                          region=regiao)
                    mouse.move(x, y)
                    pyautogui.click()
                    logging.debug('Click feito com sucesso!')
                    time.sleep(2)
                    self.tentativas(True)
                    break
                except TypeError:
                    pass
            else:
                if self.tentativa >= 100:
                    logging.debug('Botão não encontrado!')
                    self.finalizar += 1
                    logging.debug(f'Pulando [{self.finalizar}]!')
                    break
                else:
                    self.tentativas(False)

    def b_curtir(self):
        logging.debug('Botão curtir')
        logging.debug('Detectando Botão')
        while True:

            curtiron = pyautogui.locateOnScreen(Program.curtiron, confidence=0.8)

            if curtiron:
                x, y = pyautogui.locateCenterOnScreen(Program.curtiron, confidence=0.8)
                pyautogui.moveTo(x, y, 1, pyautogui.easeOutQuad)
                pyautogui.click()
                self.count += 1
                Program.mudar_pag()
                self.tentativas(True)
                logging.debug('Curtido com sucesso')
                break
            else:
                curtiroff = pyautogui.locateOnScreen(Program.curtiroff, confidence=0.8)
                if curtiroff:
                    self.count += 1
                    logging.debug('Já havia curtido, voltando!')
                    Program.mudar_pag()
                    self.tentativas(True)
                    break
                else:
                    indisponivel = pyautogui.locateOnScreen(Program.indisponivel, confidence=0.8)
                    if indisponivel:
                        pyautogui.press('f5')
                        logging.debug('Erro, corrigindo!')
                        Program.mudar_pag()
                        self.tentativas(True)
                        break
                    else:
                        indisponivel2 = pyautogui.locateOnScreen(Program.indisponivel2, confidence=0.8)
                        if indisponivel2:
                            self.testes = 0
                            self.count += 1
                            logging.debug('Já havia seguido, voltando!')
                            Program.mudar_pag()
                            self.tentativas(True)
                            break
                        else:
                            if self.tentativa >= 100:
                                logging.debug('Botão não encontrado!')
                                self.finalizar += 1
                                logging.debug(f'Pulando [{self.finalizar}]!')
                                break
                            else:
                                self.tentativas(False)

    def b_seguir(self):
        logging.debug('Botão seguir')
        logging.debug('Detectando botão')
        while True:

            seguir = pyautogui.locateOnScreen(Program.seguir, confidence=0.8)
            if seguir:
                try:
                    x, y = pyautogui.locateCenterOnScreen(Program.seguir, confidence=0.8)
                    mouse.move(x, y)
                    pyautogui.click()
                    self.count += 1
                    logging.debug('Seguido com sucesso!')
                    Program.mudar_pag()
                    self.tentativas(True)
                    break
                except TypeError:
                    pass
            else:
                indisponivel = pyautogui.locateOnScreen(Program.indisponivel, confidence=0.8)
                if indisponivel:
                    pyautogui.press('f5')
                    logging.debug('Erro, corrigindo!')
                    Program.mudar_pag()
                    break
                else:
                    indisponivel2 = pyautogui.locateOnScreen(Program.indisponivel2, confidence=0.8)
                    if indisponivel2:
                        self.tentativas(True)
                        self.count += 1
                        logging.debug('Já havia seguido, voltando!')
                        Program.mudar_pag()
                        break
                    else:
                        seguindo = pyautogui.locateOnScreen(Program.seguindo, confidence=0.8)
                        if seguindo:
                            self.tentativas(True)
                            self.count += 1
                            logging.debug('Erro, corrigindo!')
                            Program.mudar_pag()
                            break
                        else:
                            solicitado = pyautogui.locateOnScreen(Program.solicitado, confidence=0.8)
                            if solicitado:
                                self.tentativas(True)
                                self.count += 1
                                logging.debug('já havia seguido, voltando!')
                                Program.mudar_pag()
                                break
                            else:
                                if self.tentativa >= 100:
                                    logging.debug('Botão não encontrado!')
                                    self.finalizar += 1
                                    logging.debug(f'Pulando [{self.finalizar}]!')
                                    break
                                else:
                                    self.tentativas(False)

    def confirmar(self):
        logging.debug('Botão confirmar')
        logging.debug('Detectando botão')
        while True:
            confirmar = pyautogui.locateOnScreen(Program.confirmarimg, confidence=0.8)

            if confirmar:
                try:
                    x, y = pyautogui.locateCenterOnScreen(Program.confirmarimg, confidence=0.8)
                    mouse.move(x, y, multiplier=1 + random.random())
                    pyautogui.click()
                except TypeError:
                    pass
                time.sleep(1)
                for c in range(3):
                    verificar = pyautogui.locateOnScreen(Program.confirmarimg, confidence=0.8)
                    if verificar:
                        try:
                            mouse.move(random.randrange(100, 1000), random.randrange(100, 1000))
                            x_v, y_v = pyautogui.locateCenterOnScreen(Program.confirmarimg, confidence=0.8)
                            mouse.move(x_v, y_v, multiplier=1 + random.random())
                            pyautogui.click()
                        except TypeError:
                            pass

                time.sleep(1)

                verificar2 = pyautogui.locateOnScreen(Program.xinstelikes)
                if verificar2:
                    try:
                        x_v2, y_v2 = pyautogui.locateCenterOnScreen(Program.xinstelikes)
                        mouse.move(x_v2, y_v2)
                        pyautogui.click()
                        break
                    except TypeError:
                        pass
                else:
                    self.tentativas(True)
                    logging.debug('Confirmado com sucesso!')

                break
            else:
                if self.tentativa >= 100:
                    logging.debug('Botão não encontrado!')
                    self.finalizar += 1
                    logging.debug(f'Pulando [{self.finalizar}]!')
                    break
                else:
                    self.tentativas(False)

    def atualizar(self):
        logging.debug('Botão atualizar')
        logging.debug('Detectando botão')
        while True:
            atualizar = pyautogui.locateOnScreen(Program.atualizarimg, confidence=0.8)
            if atualizar:
                try:
                    x, y = pyautogui.locateCenterOnScreen(Program.atualizarimg, confidence=0.8)
                    mouse.move(x, y)
                    pyautogui.click()
                    logging.debug('Atualizado com sucesso!')
                    self.count = 0
                    self.tentativas(True)
                    break
                except TypeError:
                    pass
            else:
                if self.tentativa >= 100:
                    logging.debug('Botão não encontrado!')
                    self.finalizar += 1
                    logging.debug(f'Pulando [{self.finalizar}]!')
                    break
                else:
                    self.tentativas(False)

    @staticmethod
    def mudar_pag():
        logging.debug('Mudando a pagina!')
        while True:
            instax = pyautogui.locateOnScreen(Program.xpag, confidence=0.7)

            if instax:
                try:
                    x_i, y_i = pyautogui.locateCenterOnScreen(Program.xpag,
                                                              confidence=0.8,
                                                              region=(464, 10, 11, 12))
                    pyautogui.moveTo(x_i, y_i, 1, pyautogui.easeOutQuad)
                    pyautogui.click()
                    logging.debug('Sucesso!')
                    break
                except TypeError:
                    pass

    def tentativas(self, feito=False):
        if not feito:
            if self.tentativa >= 100:
                self.tentativa = 1
            else:
                self.tentativa += 1

        else:
            self.tentativa = 0
