import os
import PySimpleGUI as Sg
from texto import texto
from cryptography.fernet import Fernet


def deskrypto(key, aux):
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
            [Sg.Text('token', size=(5, 0)), Sg.Input(size=(65, 0), key='token')],
            [Sg.Checkbox('manter key', key='manter')],
            [Sg.Button('Deskrypto', button_color=(button1, button2)), Sg.Button('Voltar', button_color=(button1, button2))]
        ]

        janela = Sg.Window("Krypto", layout, icon='icon.ico')

        button, values = janela.Read()

        if button == 'Voltar':
            janela.hide()
            return
        if button == 'Deskrypto':
            key = values['key']
            f = Fernet(key)
            janela.hide()
            token = bytes(values['token'], 'utf-8')
            texto(f.decrypt(token), aux)
            if not values['manter']:
                break
            else:
                key = values['key']

        if button == Sg.WIN_CLOSED or button == 'Exit':
            os._exit(0)
