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

            if self.janela1 == self.janela:
                if self.eventos in ('seguir', 'curtir'):
                    self.modo = str(self.eventos)
                    self.janela1.close()
                    self.janela2 = self.layouts(2)
                    print('>>> Mude para a janela e aperte: Iniciar')
                    print(f'>>> Modo: {self.modo.upper()} selecionado')

            if self.janela2 == self.janela:
                if self.eventos == 'Iniciar':
                    self.janela2['Iniciar'].update(disabled=True, text='Aperte Esc para sair')
                    if __name__ == ('__mp_main__' or '__main__'):
                        freeze_support()
                        self.programa = Process(target=Program, args=(self.modo,))
                        self.programa.daemon = False
                        self.programa.run()
                        self.janela2['Iniciar'].update(disabled=False, text='Iniciar')

            if self.eventos == Sg.WINDOW_CLOSED:
                print(self.programa)
                sys.exit()

    @staticmethod
    def layouts(n=1):
        if n == 1:
            titlebar = [
                [Sg.Text('Instebot', background_color='#141414', text_color='#F2008C', pad=(430, 0))]
            ]

            layout1 = [[Sg.Column(layout=titlebar,
                                  expand_x=True,
                                  background_color='#141414',
                                  grab=False, pad=((0, 0), (0, 0)))],

                       [
                           Sg.Button(image_filename=Interface.follow_img, key='seguir', button_color='white'),
                           Sg.Button(image_filename=Interface.like_img, key='curtir', button_color='white')],

                       ]

            return Sg.Window('Ghoosty',
                             layout=layout1,
                             finalize=True,
                             margins=(0, 0),
                             resizable=False,
                             keep_on_top=True,
                             icon=Interface.icon,
                             no_titlebar=False,
                             grab_anywhere=True
                             )

        if n == 2:
            titlebar = [
                [Sg.Text('Instebot', background_color='#141414', text_color='#F2008C', pad=(130, 0))
                 ]

            ]

            layout2 = [
                [Sg.Column(layout=titlebar,
                           expand_x=True,
                           background_color='#141414',
                           grab=False, pad=((0, 0), (0, 0)))],

                [Sg.Output(size=(40, 20), text_color='#B7006E')],
                [Sg.Button('Iniciar', size=(37, 0), key='Iniciar', enable_events=True)],

            ]

            return Sg.Window('Ghoosty',
                             layout=layout2,
                             finalize=True,
                             location=(-3, 660),
                             keep_on_top=True,
                             disable_minimize=True,
                             grab_anywhere=True,
                             resizable=False,
                             margins=(-1, -1),
                             no_titlebar=False,
                             icon=Interface.icon,)


def iniciar():
    interface = Process(target=Interface)
    interface.daemon = True
    interface.start()

    while True:
        if str(interface).count('stopped') == 1:
            break
        if keyboard.is_pressed('Esc'):
            break


if __name__ == '__main__':
    freeze_support()
    iniciar()
