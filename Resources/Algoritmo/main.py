from cryptography.fernet import Fernet
from cript.chave import chave
from cript.descriptografar import descripto

print("Krypto")
menu = input("[1] Criptografar\n[2] Descriptografar\n[3] Sair\n")

if menu == '1':
    chave()
if menu == '2':
    key = input("Key:")
    f = Fernet(key)

    descripto(f)
if menu == '3':
    exit(0)
