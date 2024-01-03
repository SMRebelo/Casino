import sys
import time
import os
import random

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
    clear()
    write_title("Lotaria")
    write_title("Comprar Bilhete")
    try:
        num = int(input("Escolha um número de 1000 a 9999: "))
        user_filename = f"{user.nome}_jogada.txt"
        if os.path.exists(user_filename):
            with open(user_filename, 'r') as user_file:
                user_numbers = {line.strip() for line in user_file.readlines()}
                if str(num) in user_numbers:
                    print("Erro! Este número já foi escolhido pelo usuário.")
                    time.sleep(2)
                    clear()
                    jogar_lotaria(user,users)
                    return
        else:
            user_numbers = set()
        if not 1000 <= num < 10000:
            print("Escolha um número entre 1000 e 9999")
            time.sleep(2)
            clear()
            jogar_lotaria(user,users)
            return
        all_user_numbers = set()
        for filename in os.listdir():
            if filename.endswith("_jogada.txt") and filename != user_filename:
                with open(filename, 'r') as other_user_file:
                    user_numbers_other = {int(line.strip()) for line in other_user_file.readlines()}
                    all_user_numbers.update(user_numbers_other)

        if num in all_user_numbers:
            print("Erro! Este número já foi escolhido por outro jogador.")
            time.sleep(2)
            clear()
            jogar_lotaria(user,users)
            return
        
        todas_linhas = []
        with open('register.txt', 'r') as file:
            todas_linhas = file.readlines()

        for i, linha in enumerate(todas_linhas):
            partes = linha.split()
            if len(partes) >= 7 and partes[0] == user.nome:
                clear()
                pagamento = input("O Bilhete tem um custo de 5 tokens! Deseja continuar? Y/N\n")
                if pagamento.lower() == "y":
                    saldo_atual = int(partes[7])
                    if saldo_atual >= 5:
                        partes[7] = str(saldo_atual - 5)
                        todas_linhas[i] = " ".join(partes) + "\n"
                        clear()

                        with open('register.txt', 'w') as file:
                            file.writelines(todas_linhas)
                        print(f"Saldo Atualizado com sucesso!")
                        time.sleep(2)
                        
                        with open(user_filename, 'a') as user_file:
                            user_file.write(f"{str(num)}\n")
                        num = str(num)
                        print(f"Bilhetes atualizados com sucesso!")
                        time.sleep(2)
                        menu_lotaria(user,users)
                        return
                    
                    else:
                        print("Erro! Não tem saldo!")
                        time.sleep(2)
                        comprar_tokens(user, users)
                        return
                else:
                    clear()
                    print("Check-out vazio!")
                    time.sleep(2)
                    menu_lotaria(user,users)
    except ValueError:
        print('Valor inválido! Tente novamente')
        time.sleep(2)
        clear()
        jogar_lotaria(user,users)


    
  
def sorteio(user, users):
    from saldo import limpar_conteudo_arquivos_jogada
    clear()
    num_premio = 1212

    write_title("Domingo anda à Roda!!!")
    write_title("")

    choice = input("Digite Y para começar o sorteio!\n").lower()

    if choice == "y":
        with open('register.txt', 'r') as file:
            todas_linhas = file.readlines()

        premio_2_digitos = num_premio % 1000
        premio_3_digitos = num_premio % 100

        vencedores = []

        for linha in todas_linhas:
            partes = linha.split()
            user_filename = f"{partes[0]}_jogada.txt"

            with open(user_filename, 'r') as user_file:
                jogadas_usuario = {int(line.strip()) for line in user_file.readlines()}

                if num_premio in jogadas_usuario:
                    vencedores.append(partes[0])
                elif premio_2_digitos in jogadas_usuario:
                    vencedores.append(partes[0])
                elif premio_3_digitos in jogadas_usuario:
                    vencedores.append(partes[0])

        if vencedores:
            clear()
            write_title("Vencedores Lotaria")
            for vencedor in vencedores:
                write_title(vencedor)
            time.sleep(5)
            limpar_conteudo_arquivos_jogada()
            clear()
            menu_lotaria(user, users)
        else:
            print("Não há vencedores :(")
            time.sleep(2)
            clear()
            menu_lotaria(user, users)

    else:
        print("Obrigado por não rodar")
        time.sleep(2)
        clear()
        menu_lotaria(user, users)