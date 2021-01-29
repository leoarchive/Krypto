from cryptography.fernet import Fernet
from cript.criptografar import cripto

def chave():
    menu = input("[1] Criar nova chave\n[2] Usar outra chave\n")

    if menu == '1':
        key = Fernet.generate_key()
        f = Fernet(key)
        cripto(f, key)
    if menu == '2':
        key = input("Key:")
        f = Fernet(key)
        cripto(f, key)
