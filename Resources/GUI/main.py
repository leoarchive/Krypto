import os
import PySimpleGUI as Sg
from chave import chave
from deskryptografar import deskrypto


def krypto():
    Sg.theme('SystemDefaultForReal')
    button1 = 'black'
    button2 = 'grey94'
    logo = r'L:\Usuarios\ProjetosPython\GUI\img\Krypto.png'
    aux = 1

    while 1:
        if aux == 1:
            tema = 'Darkmode'
        else:
            tema = 'Whitemode'
        layout = [
            [Sg.Button(tema, font=('Calibri Bold', 9), size=(10, 0))]
        ]
        layout += [
            [Sg.Image(logo)],
            [Sg.Button('Criptografar', font=('Calibri Bold', 13), size=(60, 1), border_width=0, button_color=(button1, button2))],
            [Sg.Button('Descriptografar', font=('Calibri Bold', 13), size=(60, 1), border_width=0, button_color=(button1, button2))],
            [Sg.Button('Sair', font=('Calibri Bold', 13), size=(60, 1), border_width=0, button_color=(button1, button2))]
        ]

        janela = Sg.Window("Krypto", layout, icon='icon.ico', finalize=True)
        button, values = janela.Read()

        if button == 'Descriptografar':
            janela.hide()
            key = 'key'
            deskrypto(key, aux)
        if button == 'Criptografar':
            janela.hide()
            chave(aux)
        if button == 'Sair':
            os._exit(0)
        if button == 'Darkmode':
            theme = 'DarkBlack'
            button1 = 'grey94'
            button2 = 'black'
            logo = r'L:\Usuarios\ProjetosPython\GUI\img\KryptoDark.png'
            aux = -1
            janela.hide()
        else:
            theme = 'SystemDefaultForReal'
            button1 = 'black'
            button2 = 'grey94'
            logo = r'L:\Usuarios\ProjetosPython\GUI\img\Krypto.png'
            aux = 1
            janela.close()
        Sg.theme(theme)
        if button == Sg.WIN_CLOSED or button == 'Exit':
            os._exit(0)


krypto()
