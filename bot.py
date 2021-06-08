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
        print(f'{datetime.datetime.today().hour}:{datetime.datetime.today().minute}:{datetime.datetime.today().second}'
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

    def __init__(self, modo):
        self.count = 0  # numero de trades finalizadas
        self.testes = 0  # faz 20 testes e se não encontrar finaliza
        self.update = random.randint(3, 8)
        self.modo = modo

        logging.debug('Aperte Esc para sair!!')
        try:
            logging.debug('Iniciando programa.')
            while True:
                if self.count >= self.update:
                    Program.atualizar(self)
                Program.b_ganharmoedas(self)
                if modo == 'seguir':
                    Program.b_seguir(self)
                elif modo == 'curtir':
                    Program.b_curtir(self)
                Program.confirmar()
        except KeyboardInterrupt:
            logging.debug('Finalizando programa.')
            sys.exit()

    '''def iniciar_text(self):
        print('|==== Selecione o modo ====|')
        print('|[1] PARA SEGUIR' + (' ' * 11) + '|')
        print('|[2] PARA CURTIR' + (' ' * 11) + '|')
        self.mode = input('=> ')
        while self.mode not in ('1', '2'):
            self.mode = input('=> ')
        if self.mode == '1':
            print('MODO SEGUIR SELECIONADO!', flush=True)
        elif self.mode == '2':
            print('MODO CURTIR SELECIONADO', flush=True)
        time.sleep(1)
        print('MUDE PARA A TELA DO BLUESTACKS E LARGUE O MOUSE', flush=True)
        time.sleep(1)
        print('INICIANDO...', flush=True)
        time.sleep(1)'''

    def b_ganharmoedas(self):
        logging.debug('Esperando, tela....')
        while True:

            regiao = random.choice(self.lista_botoes)
            ganharmoedas = pyautogui.locateOnScreen(Program.ganharmoedas, confidence=0.9, region=regiao)
            if ganharmoedas:
                try:
                    x, y = pyautogui.locateCenterOnScreen(Program.ganharmoedas,
                                                          confidence=0.9,
                                                          region=regiao)
                    logging.debug('pegando moedas')
                    mouse.move(x, y)
                    pyautogui.click()
                    time.sleep(2)
                    self.testes = 0
                    break
                except TypeError:
                    pass

    def b_curtir(self):
        logging.debug('curtindo')
        while True:

            curtiroff = pyautogui.locateOnScreen(Program.curtiroff, confidence=0.8)
            curtiron = pyautogui.locateOnScreen(Program.curtiron, confidence=0.8)

            if curtiron:
                x, y = pyautogui.locateCenterOnScreen(Program.curtiron, confidence=0.8)
                pyautogui.moveTo(x, y, 1, pyautogui.easeOutQuad)
                pyautogui.click()
                self.count += 1
                Program.mudar_pag()
                logging.debug('curtido com sucesso')
                break
            elif curtiroff:
                self.count += 1
                logging.debug('já havia curtido, voltando!')
                Program.mudar_pag()
                break

    def b_seguir(self):
        logging.debug('seguindo')
        while True:
            seguindo = pyautogui.locateOnScreen(Program.seguindo, confidence=0.8)
            solicitado = pyautogui.locateOnScreen(Program.solicitado, confidence=0.8)
            indisponivel = pyautogui.locateOnScreen(Program.indisponivel, confidence=0.8)
            seguir = pyautogui.locateOnScreen(Program.seguir, confidence=0.8)
            if seguir:
                try:
                    x, y = pyautogui.locateCenterOnScreen(Program.seguir, confidence=0.8)
                    mouse.move(x, y)
                    pyautogui.click()
                    self.count += 1
                    logging.debug('seguido com sucesso, voltando!')
                    Program.mudar_pag()
                    self.testes = 0
                    break
                except TypeError:
                    pass

            elif indisponivel:
                self.testes = 0
                self.count += 1
                logging.debug('já havia seguido, voltando!')
                Program.mudar_pag()
                break

            elif seguindo:
                self.testes = 0
                self.count += 1
                logging.debug('já havia seguido, voltando!')
                Program.mudar_pag()
                break

            elif solicitado:
                self.testes = 0
                self.count += 1
                logging.debug('já havia seguido, voltando!')
                Program.mudar_pag()
                break

    @staticmethod
    def confirmar():
        logging.debug('confirmando')
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
                    logging.debug('confirmado com sucesso!')

                break

    def atualizar(self):
        logging.debug('atualizando')
        while True:
            atualizar = pyautogui.locateOnScreen(Program.atualizarimg, confidence=0.8)
            if atualizar:
                try:
                    x, y = pyautogui.locateCenterOnScreen(Program.atualizarimg, confidence=0.8)
                    mouse.move(x, y)
                    pyautogui.click()
                    logging.debug('atualizado com sucesso!')
                    self.count = 0
                    self.testes = 0
                    break
                except TypeError:
                    pass

    @staticmethod
    def mudar_pag():
        logging.debug('movendo pagina')
        while True:
            instax = pyautogui.locateOnScreen(Program.xpag, confidence=0.7)

            if instax:
                try:
                    x_i, y_i = pyautogui.locateCenterOnScreen(Program.xpag,
                                                              confidence=0.8,
                                                              region=(464, 10, 11, 12))
                    pyautogui.moveTo(x_i, y_i, 1, pyautogui.easeOutQuad)
                    pyautogui.click()
                    break
                except TypeError:
                    pass
