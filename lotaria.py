import sys
import time
import os

sys.path.append(r'C:\Users\sergi\OneDrive\Documents')
from functions import clear, write_menu, is_valid_name, erro_invalid, write_title, read_users, print_users



def menu_lotaria(user, users):
    from menu import menu_principal
    clear()
    opcoes = ['Comprar tokens', 'Jogar Lotaria', 'Sorteio', 'Sair']
    try: 
        num = write_menu('Lotaria', '\nEscolha uma Opção: ', opcoes)
        match num:
            case 1:
                comprar_tokens(user, users)
            case 2:
                jogar_lotaria(user, users)
            case 3:
                sorteio(user,users)
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
    from saldo import save_transaction
    clear()
    write_title('Comprar Tokens') 
    write_title(" 1 Token = 1€ ")

    todas_linhas = []
    with open('register.txt', 'r') as file:
        todas_linhas = file.readlines()

    for i, linha in enumerate(todas_linhas):
        partes = linha.split()
        if len(partes) >= (7) and partes[0] == user.nome:
            try:
                num = int(input("\nQuantos Tokens deseja comprar: "))
                partes[2] = int(partes[2]) - num
                partes[2] = str(partes[2])
                partes[7] = int(partes[7]) + num
                partes[7] = str(partes[7])
            except ValueError:
                print("Erro! Digite um valor numérico!")
                comprar_tokens(user, users)
            
            todas_linhas[i] = " ".join(partes) + "\n"
            print(f"Saldo Atualizado com sucesso!")
            time.sleep(2)
            save_transaction(user.nome, 'levantamento', num)
            print(f"Histórico Atualizado com sucesso!")

    with open('register.txt', 'w') as file:
        file.writelines(todas_linhas)
    
    menu_lotaria(user, users)
        
def jogar_lotaria(user, users):
    from saldo import jogada_lotaria
    clear()
    write_title("Lotaria")
    write_title("Comprar Bilhete")
    try:
        num = int(input("Escolha um número de 1000 a 9999: "))
        if 1000 <= num < 10000:
            todas_linhas = []
            with open('register.txt', 'r') as file:
                todas_linhas = file.readlines()
            for i, linha in enumerate(todas_linhas):
                partes = linha.split()
                if len(partes) >= 7 and partes[0] == user.nome:
                    clear()
                    pagamento = input("O Bilhete tem um custo de 5 tokens! Deseja continuar? Y/N\n")
                    if pagamento.lower() == "y":
                        if int(partes[7]) >= 5:
                            partes[7] = str(int(partes[7]) - 5)
                            todas_linhas[i] = " ".join(partes) + "\n"
                            clear()
                            print(f"Saldo Atualizado com sucesso!")
                            time.sleep(2)
                            with open('register.txt', 'w') as file:
                                file.writelines(todas_linhas)    
                            num = str(num)
                            jogada_lotaria(user.nome, num)
                            return
                        else: 
                            print("Erro! Não tem saldo!")
                            time.sleep(2)
                            comprar_tokens(user, users)
                            return
            print("Erro! Usuário não encontrado.")
        else:
            print("Escolha um número entre 1000 e 9999")
            jogar_lotaria(user, users)
    except ValueError:
        print('Valor inválido! Tente novamente')

def sorteio(user,users):
    
    
    
    
    return print("Esta quase")
    