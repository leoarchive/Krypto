import os
import PySimpleGUI as Sg
from texto import texto
from cryptography.fernet import Fernet


def kryptogra(f, key, aux):
    if aux == -1:
        theme = 'DarkBlack'
        button1 = 'grey94'
        button2 = 'black'
        logo = r'L:\Usuarios\ProjetosPython\GUI\img\KryptoDark.png'
    else:
        theme = 'SystemDefaultForReal'
        button1 = 'black'
        button2 = 'grey94'
        logo = r'L:\Usuarios\ProjetosPython\GUI\img\Krypto.png'
    Sg.theme(theme)

    while 1:
        layout = [
            [Sg.Image(logo)],
            [Sg.Text('key', size=(5, 0)), Sg.Input(key, size=(60, 0), key='key')],
            [Sg.Text('Texto', size=(5, 0)), Sg.Input(size=(60, 0), key='token')],
            [Sg.Checkbox('manter key', key='manter')],
            [Sg.Button('Krypto', button_color=(button1, button2)), Sg.Button('Voltar',  button_color=(button1, button2))]
        ]

        janela = Sg.Window("Krypto", layout, icon='icon.ico')
        button, values = janela.Read()

        if button == 'Voltar':
            janela.hide()
            return
        if button == 'Krypto':
            if f == 0:
                key = values['key']
                f = Fernet(key)
            janela.hide()
            token = values['token']
            texto(f.encrypt(bytes(token, 'utf-8')), aux)
            if not values['manter']:
                os._exit(0)
            else:
                key = values['key']

        if button == Sg.WIN_CLOSED or button == 'Exit':
            os._exit(0)
