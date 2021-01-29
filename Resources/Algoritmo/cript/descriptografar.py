import os


def descripto(f):
    os.system("cls")

    texto = input("Token:\n")
    token = bytes(texto, 'utf-8')
    print("Texto descriptografado:", f.decrypt(token))
    os.system("pause")
