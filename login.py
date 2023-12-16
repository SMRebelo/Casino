import os.path
import os
import sys
import time
from menu import menu_principal
from user import User

sys.path.append(r'C:\Users\sergi\OneDrive\Documents')
from functions import clear, write_menu, is_valid_name, erro_invalid, write_title, print_users, read_users

if not os.path.exists('register.txt'):
    file = open('register.txt', 'w')
    file.close()

global users
users = []

def register():
    global users

    username = input("Escreva o seu nome: ")
    if is_valid_name(username):
        try:
            with open('register.txt', 'r') as file:
                if username in file.read():
                    print("Erro! Este utilizador já existe!")
                    sys.exit(1)
            password = input("Digite a password: ")
            password2 = input("Confirme a password: ")
            if password == "":
                print("Erro! A password não pode estar vazia!")
            else:
                if password != password2:
                    print("Erro! Password errada")
                    sys.exit(1)
                else:
                    try:
                        user = User(username, password, 100, 0, 0, 0, 0, 0)
                        users.append(user)
                        with open('register.txt', 'a') as file:
                            file.write(f"{user.nome} {user.senha} {user.saldo} {user.score_lot} {
                                       user.score_quiz} {user.score_rasp1} {user.score_rasp2} {user.tokens}\n")
                        time.sleep(2)
                        menu_principal(user, users)

                    except Exception as e:
                        print(f"Erro: {e}")
        except Exception as e:
            print(f"Erro: {e}")
    else:
        print("Erro! Utilize apenas letras")

def login():
    global users

    clear()
    while True:
        write_title("Log-In")
        username = input("Digite o nome de usuário: ")
        password = input("Digite a password: ")
        lista = []
        with open('register.txt', 'r') as file:
            for line in file:
                lista.append(line.split())

        total_users = len(lista)
        login_sucesso = 0
        cont = 0

        while cont < total_users:
            if len(lista[cont]) >= 2:
                usernames = lista[cont][0]
                passwords = lista[cont][1]
                if username == usernames and password == passwords:
                    login_sucesso = 1
                    user = User(username, password, 100, 0, 0, 0, 0, 0)
                    break
                else:
                    print("Erro! Dados Errados!")
                    time.sleep(0.5)
                    clear()
                    cont += 1
            else:
                print("Erro! Conta não está no arquivo!")
                pergunta = input("Deseja criar uma conta? Digite Sim/Nao : ")
                if is_valid_name(pergunta):
                    if pergunta.lower() == "sim":
                        register()
                    elif pergunta.lower() == "nao":
                        clear()
                        continue
                    else:
                        print(erro_invalid())
                        sys.exit(1)

        if login_sucesso == 1:

            clear()
            print("\nLog In realizado com sucesso!")
            print(f"\nBem Vindo {username}")
            time.sleep(0.5)
            clear()
            menu_principal(user, users)
            break


def boas_vindas():
    clear()
    print("\n\n              Bem Vindo!\n\n\n")
    time.sleep(0.5)
    clear()
    print("-"*30)
    print("<<<<<<<<<<<-CASINO->>>>>>>>>>>")
    print("-"*30)
    try:
        registo = int(input("\n[1]-Registar\n[2]-Log IN\n\n[0]-Sair\n"))
        match registo:
            case 1:
                clear()
                register()
            case 2:
                clear()
                login()
            case 0:
                clear()
                print("Obrigado por visitar o CASINO")
                time.sleep(2)
                sys.exit(1)
    except ValueError:
        print("Erro! Valor inválido!")


boas_vindas()
