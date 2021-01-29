import os
import PySimpleGUI as Sg


def erro(aux):
    if aux == -1:
        theme = 'DarkBlack'
        button1 = 'grey94'
        button2 = 'black'
    else:
        theme = 'SystemDefaultForReal'
        button1 = 'black'
        button2 = 'grey94'
    Sg.theme(theme)

    while 1:
        layout = [
            [Sg.Text('Aí, não tem como fazer as duas coisas ao mesmo tempo')],
            [Sg.Button('Voltar', button_color=(button1, button2))]
        ]

        janela = Sg.Window("Krypto", layout, icon='icon.ico')

        button, values = janela.Read()
        if button == 'Voltar':
            janela.hide()
            return

        if button == Sg.WIN_CLOSED or button == 'Exit':
            os._exit(0)
