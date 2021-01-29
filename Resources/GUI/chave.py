import os
import PySimpleGUI as Sg
from kriptografar import kryptogra
from error import erro
from cryptography.fernet import Fernet


def chave(aux):
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
            [Sg.Checkbox('Nova key', key='nova'), Sg.Checkbox('Outra key', key='manter')],
            [Sg.Button('Ok', button_color=(button1, button2)), Sg.Button('Voltar', button_color=(button1, button2))]
        ]

        janela = Sg.Window("Krypto", layout, icon='icon.ico')

        button, values = janela.Read()

        if values['nova']:
            if values['manter']:
                janela.close()
                erro(aux)
                values['manter'] = False
                values['nova'] = False
                button = 0

        if button == 'Voltar':
            janela.hide()
            return
        if button == 'Ok':
            if values['nova']:
                janela.hide()
                key = Fernet.generate_key()
                f = Fernet(key)
                kryptogra(f, key, aux)
            if values['manter']:
                janela.hide()
                key = 'Key'
                f = 0
                kryptogra(f, key, aux)
            if values['manter'] == False and values['nova'] == False:
                janela.close()
                erro(aux)

        if button == Sg.WIN_CLOSED or button == 'Exit':
            os._exit(0)
