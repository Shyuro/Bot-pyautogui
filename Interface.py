import sys
from bot import Program
import PySimpleGUI as Sg
from threading import Thread


class Interface:
    def __init__(self):
        Sg.theme_global('Black')
        self.status = 'run'
        self.janela1, self.janela2 = self.layouts(1), None

        while True:
            self.janela, self.eventos, self.valores = Sg.read_all_windows()

            if self.eventos in ('seguir', 'curtir'):
                self.janela1.close()
                self.janela2 = self.layouts(2)
                programa = Thread(target=Program, args=(self.eventos,))
                programa.start()


            if self.eventos == Sg.WINDOW_CLOSED:
                sys.exit()

    @staticmethod
    def layouts(n=1):
        if n == 1:
            layout1 = [
                [Sg.Button(image_filename='follow.png', key='seguir'),
                 Sg.Button(image_filename='like.png', key='curtir')]
            ]
            return Sg.Window('Instelikes-bot', layout=layout1, finalize=True)

        if n == 2:
            layout2 = [
                [Sg.Output(size=(30, 20))]
            ]
            return Sg.Window('Instelikes-bot',
                             layout=layout2,
                             finalize=True,
                             location=(-6, 717),
                             keep_on_top=True,
                             disable_minimize=True,)
