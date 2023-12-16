import sys
import time
import os

sys.path.append(r'C:\Users\sergi\OneDrive\Documents')
from functions import clear, write_menu, is_valid_name, erro_invalid, write_title, read_users, print_users

def menu_lotaria(user, users):
    from menu import menu_principal
    clear()
    opcoes = ['Comprar tokens', 'Jogar Lotaria', 'Sair']
    try: 
        num = write_menu('Lotaria', '\nEscolha uma Opção: ', opcoes)
        match num:
            case 1:
                comprar_tokens(user, users)
            case 2:
                jogar_lotaria(user, users)
            case 0:
                menu_principal(user, users)
            case _:
                print("Erro! Opção inválida!")
                time.sleep(2)
                menu_lotaria(user, users)
    except ValueError:
        print("Erro! Opção inválida!")
        menu_lotaria(user, users)

def comprar_tokens(user, users):
    clear()
    write_title('Comprar Tokens') 
    write_title(" 1 Token = 1€ ")
    
    todas_linhas = []
    with open('register.txt', 'r') as file:
        todas_linhas = file.readlines()

    with open('register.txt', 'w') as file:
        for linha in todas_linhas:
            partes = linha.split()
            if len(partes) >= (7) and partes[0] == user.nome:
                try:
                    num = int(input("\nQuantos Tokens deseja comprar: "))
                    partes[2] = int(partes[2]) - (num*5)
                    partes[2] = str(partes[2])
                    partes[7] = int(partes[7]) + num
                    partes[7] = str(partes[7])
                except ValueError:
                    print("Erro! Digite um valor numérico!")
                    comprar_tokens(user, users)
                    
                nova_linha = " ".join(partes) + "\n"
                file.write(nova_linha)
                print(f"Saldo Actualizado com sucesso!")
                time.sleep(2)
                with open('saldo.txt', 'a') as file:
                    file.write(f"-{num*5}\n")       
                menu_lotaria(user, users)        
     
    
    

    