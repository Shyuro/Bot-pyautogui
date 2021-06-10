import sys
from bot import Program, resource_path0
import PySimpleGUI as Sg
from multiprocessing import Process, freeze_support
import keyboard

Sg.LOOK_AND_FEEL_TABLE['MyColors'] = {'BACKGROUND': '#DB1E71',
                                      'TEXT': '#000000',
                                      'INPUT': '#191919',
                                      'TEXT_INPUT': '#000000',
                                      'SCROLL': '#000000',
                                      'BUTTON': ('#000000', '#FF087C'),
                                      'PROGRESS': Sg.DEFAULT_PROGRESS_BAR_COLOR,
                                      'BORDER': 0, 'SLIDER_DEPTH': 0,
                                      'PROGRESS_DEPTH': 0,
                                      'ACCENT1': '#000000',
                                      'ACCENT2': '#000000',
                                      'ACCENT3': '#000000'}


class Interface:
    follow_img = resource_path0('interface_imagens/follow.png')
    like_img = resource_path0('interface_imagens/like.png')
    icon = resource_path0('interface_imagens/icon.ico')

    def __init__(self):
        Sg.theme('MyColors')
        self.tela = False

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
                if __name__ == '__main__':
                    freeze_support()
                    programa = Process(target=Program, args=(self.modo,))
                    programa.daemon = True
                    programa.run()

            if self.eventos == Sg.WINDOW_CLOSED:
                sys.exit()

    @staticmethod
    def layouts(n=1):
        if n == 1:
            titlebar = [
                [Sg.Text('Ghoosty - Instebot', background_color='#141414', text_color='#F2008C', pad=(400, 0))]
            ]
            downbar = [
                [Sg.Text('*Aperte esc para sair', background_color='#B72C6D', text_color='#000000', pad=(400, 0))]
            ]
            layout1 = [[Sg.Column(layout=titlebar,
                                  expand_x=True,
                                  background_color='#141414',
                                  grab=True, pad=((0, 0), (0, 0)))],

                       [
                           Sg.Button(image_filename=Interface.follow_img, key='seguir', button_color='white'),
                           Sg.Button(image_filename=Interface.like_img, key='curtir', button_color='white')],

                       [Sg.Column(layout=downbar,
                                  expand_x=True,
                                  background_color='#B72C6D',
                                  pad=((0, 0), (0, 0)))],
                       ]

            return Sg.Window('Ghoosty - Instebot',
                             layout=layout1,
                             finalize=True,
                             margins=(0, 0),
                             resizable=False,
                             keep_on_top=True,
                             no_titlebar=True,
                             grab_anywhere=True)

        if n == 2:
            titlebar = [
                [Sg.Text('Ghoosty - Instebot', background_color='#141414', text_color='#F2008C', pad=(100, 0))
                 ]

            ]

            layout2 = [
                [Sg.Column(layout=titlebar,
                           expand_x=True,
                           background_color='#141414',
                           grab=True, pad=((0, 0), (0, 0)))],

                [Sg.Text('*Aperte Esc para sair!'), Sg.Text(' ' * 27), Sg.Button('Iniciar')],
                [Sg.Output(size=(40, 20), text_color='#B7006E')]
            ]

            return Sg.Window('Ghoosty - Instebot',
                             layout=layout2,
                             finalize=True,
                             location=(-3, 660),
                             keep_on_top=True,
                             grab_anywhere=True,
                             resizable=False,
                             margins=(-1, -1),
                             no_titlebar=True, )


def iniciar():
    interface = Process(target=Interface)
    interface.daemon = True
    interface.start()
    while True:
        if keyboard.is_pressed('Esc'):
            break


if __name__ == '__main__':
    freeze_support()
    iniciar()
