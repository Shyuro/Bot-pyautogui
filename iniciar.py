import keyboard
from Interface import Interface
from threading import Thread


def iniciar():
    interface = Thread(target=Interface)
    interface.daemon = True
    interface.start()
    while True:
        if keyboard.is_pressed('Esc'):
            break


iniciar()
