from utils import *
from bruteforce import *
from defs import *

senha = None
hash_senha = None

while True:

    print("""
    1 - Verificar Força
    2 - Gerar Hash
    3 - Verificar Hash
    4 - Demonstrar brute force
    5 - Vazamentos
    6 - sair
    """)

    opcao = input("Escolha: ")

    if opcao == "1":
        senha = input("Digite a sua senha: ")

        pontos = verificar_forca(senha)
        barra_forca(pontos)
        mostrar_forca(pontos)

    elif opcao == "2":
        if senha is None:
            print("Primeiro define uma senha na opção 1")
        else:
            hash_senha = gerar_hash(senha)
            print(f"Hash: {hash_senha}")
            salvar_hash(hash_senha)

    elif opcao == "3":
        senha_verificar = input("Digite a senha para verificar: ")
        hash_verificar = input("Digite o hash: ")

        try:
            if verificar_hash(senha_verificar, hash_verificar):
                print("Senha verificada!")
            else:
                print("Senha incorreta!")
        except ValueError:
            print("Hash inválida!")

    elif opcao == "4":
        if senha is None:
            print("Define uma senha primeiro.")
        else:
            brute_force_demo(senha)

    elif opcao == "5":

        senha = input("Digite a senha: ")

        vazamentos = verificar_vazamento(senha)

        if vazamentos:

            print(
                f"Senha encontrada em {vazamentos} vazamentos!"
            )

        else:

            print("Senha não encontrada em vazamentos.")

    elif opcao == "6":
        break

    else:
        print("Opção inválida")