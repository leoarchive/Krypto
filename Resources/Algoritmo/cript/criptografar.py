import os


def cripto(f, key):

    while True:
        os.system("cls")

        print(key)

        texto = input("Digite o texto para criptografia:")
        token = f.encrypt(bytes(texto, 'utf-8'))
        print("Texto criptografado:", f.decrypt(token))

        confirmar = input("[1] Confirmar\n[2] Nova tentativa\n[3] Sair\n")
        if confirmar == '1':
            print("Texto criptografado:", token)
            os.system("pause")
        if confirmar == '3':
            exit(0)