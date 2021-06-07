import sys
import time
import pyautogui
import random
import logging
from pyHM import mouse


class Program:

    lista_botoes = [
        (411, 524, 114, 29), (843, 524, 114, 29), (1274, 524, 114, 29), (1706, 524, 114, 29),
        (411, 823, 114, 29), (843, 823, 114, 29), (1274, 823, 114, 29), (1706, 823, 114, 29)
    ]

    logging.basicConfig(level=logging.DEBUG,
                        format='%(asctime)s %(levelname)s: %(message)s')

    def __init__(self, modo):
        self.count = 0  # numero de trades finalizadas
        self.testes = 0  # faz 20 testes e se não encontrar finaliza
        self.update = random.randint(3, 8)
        self.modo = modo

        try:
            logging.debug('Iniciandorograma.')
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
            logging.debug('Finalizandorograma.')
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
        logging.debug('pegando moedas')
        while True:

            regiao = random.choice(self.lista_botoes)
            ganharmoedas = pyautogui.locateOnScreen('img/ganharmoedas.bmp', confidence=0.9, region=regiao)
            if ganharmoedas:
                try:
                    x, y = pyautogui.locateCenterOnScreen('img/ganharmoedas.bmp',
                                                          confidence=0.9,
                                                          region=regiao)
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

            curtiroff = pyautogui.locateOnScreen('img/curtiroff.png', confidence=0.8)
            curtiron = pyautogui.locateOnScreen('img/curtiron.png', confidence=0.8)

            if curtiron:
                x, y = pyautogui.locateCenterOnScreen('img/curtiron.png', confidence=0.8)
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
            seguindo = pyautogui.locateOnScreen('img/seguindo.png', confidence=0.8)
            solicitado = pyautogui.locateOnScreen('img/solicitado.png', confidence=0.8)
            indisponivel = pyautogui.locateOnScreen('img/indisponivel.png', confidence=0.8)
            seguir = pyautogui.locateOnScreen('img/seguir.png', confidence=0.8)
            if seguir:
                try:
                    x, y = pyautogui.locateCenterOnScreen('img/seguir.png', confidence=0.8)
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
            confirmar = pyautogui.locateOnScreen('img/confirmar.png', confidence=0.8)

            if confirmar:
                try:
                    x, y = pyautogui.locateCenterOnScreen('img/confirmar.png', confidence=0.8)
                    mouse.move(x, y, multiplier=1 + random.random())
                    pyautogui.click()
                except TypeError:
                    pass
                time.sleep(1)
                for c in range(3):
                    verificar = pyautogui.locateOnScreen('img/confirmar.png', confidence=0.8)
                    if verificar:
                        try:
                            mouse.move(random.randrange(100, 1000), random.randrange(100, 1000))
                            x_v, y_v = pyautogui.locateCenterOnScreen('img/confirmar.png', confidence=0.8)
                            mouse.move(x_v, y_v, multiplier=1 + random.random())
                            pyautogui.click()
                        except TypeError:
                            pass

                time.sleep(1)

                verificar2 = pyautogui.locateOnScreen('img/xinstelikes.png')
                if verificar2:
                    try:
                        x_v2, y_v2 = pyautogui.locateCenterOnScreen('img/xinstelikes.png')
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
            atualizar = pyautogui.locateOnScreen('img/atualizar.png', confidence=0.8)
            if atualizar:
                try:
                    x, y = pyautogui.locateCenterOnScreen('img/atualizar.png', confidence=0.8)
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
            instax = pyautogui.locateOnScreen('img/xpag.png', confidence=0.7)

            if instax:
                try:
                    x_i, y_i = pyautogui.locateCenterOnScreen('img/xpag.png',
                                                              confidence=0.8,
                                                              region=(464, 10, 11, 12))
                    pyautogui.moveTo(x_i, y_i, 1, pyautogui.easeOutQuad)
                    pyautogui.click()
                    break
                except TypeError:
                    pass


iniciar = Program
iniciar('seguir')
