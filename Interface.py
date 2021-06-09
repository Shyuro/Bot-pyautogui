import sys
from bot import Program, resource_path0
import PySimpleGUI as Sg
from multiprocessing import Process
import keyboard


class Interface:
    follow_img = resource_path0('interface_imagens/follow.png')
    like_img = resource_path0('interface_imagens/like.png')
    icon = resource_path0('interface_imagens/icon.ico')

    def __init__(self):
        Sg.theme_global('Reddit')
        self.janela1, self.janela2 = self.layouts(1), None

        while True:
            self.janela, self.eventos, self.valores = Sg.read_all_windows()

            if self.eventos in ('seguir', 'curtir'):
                self.modo = str(self.eventos)
                self.janela1.close()
                self.janela2 = self.layouts(2)
                print('>>> Mova para a janela e aperte: Iniciar')

            if self.eventos == 'Iniciar':
                self.janela2['Iniciar'].update(disabled=True)
                print(f'>>> MODO: {self.modo} selecionado')
                programa = Process(target=Program, args=(self.modo,))
                programa.daemon = True
                programa.run()

            if self.eventos == Sg.WINDOW_CLOSED:
                sys.exit()

    @staticmethod
    def layouts(n=1):
        if n == 1:
            layout1 = [
                [Sg.Button(image_filename=Interface.follow_img, key='seguir', button_color='white'),
                 Sg.Button(image_filename=Interface.like_img, key='curtir', button_color='white')]
            ]
            return Sg.Window('Mr Insta', layout=layout1, finalize=True, icon=Interface.icon)

        if n == 2:
            layout2 = [
                [Sg.Text('Aperte Esc para sair!'), Sg.Text(' ' * 27), Sg.Button('Iniciar')],
                [Sg.Output(size=(40, 20), text_color='blue')]
            ]
            return Sg.Window('Mr Insta',
                             layout=layout2,
                             finalize=True,
                             location=(-6, 717),
                             keep_on_top=True,
                             disable_minimize=True,
                             icon=Interface.icon,
                             disable_close=True)


def iniciar():
    interface = Process(target=Interface)
    interface.daemon = True
    interface.start()
    while True:
        if keyboard.is_pressed('Esc'):
            break


if __name__ == '__main__':
    iniciar()
