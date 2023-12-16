from menu import menu_principal
from functions import clear, write_menu, is_valid_name, erro_invalid, write_title
import sys
import time

sys.path.append(r'C:\Users\sergi\OneDrive\Documents')


def menu_gestao(user, users):
    clear()
    lista = ['Editar User', 'Apagar User', 'Apagar Rank', 'Menu']
    choice = write_menu("Gestão de Conta", "\nEscolha uma Opção: ", lista)
    match choice:
        case 1:
            edit_user(user, users)
        case 2:
            delete_user(user, users)
        case 3:
            delete_all(user, users)
        case 0:
            menu_principal(user, users)
        case _:
            print("Erro! Opção inválida!")
            time.sleep(2)
            menu_gestao(user, users)


def edit_user(user, users):
    clear()
    write_title("Editar Usuário")
    new_name = input("Digite o novo User: ")
    new_pass = input("Digite uma nova Password: ")
    if is_valid_name(new_name) and new_pass != "":
        lista = []
        with open('register.txt', 'r') as file:
            if new_name in file.read():
                print("Erro! Este utilizador já existe!")
                time.sleep(2)
                menu_gestao(user, users)

        with open('register.txt', 'r') as file:
            for line in file:
                lista.append(line.split())

        total_users = len(lista)
        encontrada = False
        cont = 0

        while cont < total_users:
            if len(lista[cont]) >= 2:
                username = lista[cont][0]
                password = lista[cont][1]
                if username == user.nome and password == user.senha:
                    lista[cont][0] = new_name
                    lista[cont][1] = new_pass
                    encontrada = True
                    break
                cont += 1
            else:
                print("Erro! Conta não está no arquivo!")

        if encontrada == True:
            with open('register.txt', 'w') as file:
                for linha in lista:
                    line = ' '.join(linha) + '\n'
                    file.write(line)
            print("Usuário editado com sucesso!")
            time.sleep(2)
            menu_gestao(user, users)
        else:
            print("Erro! Conta não está no arquivo!")
            time.sleep(2)
            menu_gestao(user, users)
    else:
        print("Erro! Dados inválidos!")


def delete_user(user, users):
    clear()
    write_title("Eliminar Usuário")
    choice = input("Tem a certeza que deseja eliminar este Usuário? Sim/Nao: ")
    if choice == "sim":
        todas_linhas = []
        with open('register.txt', 'r') as file:
            todas_linhas = file.readlines()

        with open('register.txt', 'w') as file:
            eliminada = False
            for linha in todas_linhas:
                if linha.split()[0] != user.nome:
                    file.write(linha)
                else:
                    eliminada = True
            if eliminada == True:
                print("Conta Eliminada com sucesso!")
                time.sleep(2)
                menu_gestao(user, users)
            else:
                print("Erro! Conta não encontrada.")
    elif choice == "nao":
        menu_gestao(user, users)
    else:
        print("Erro! Opção errada!")
        time.sleep(2)
        menu_gestao(user, users)


def delete_all(user, users):
    clear()
    opcoes = ['Quiz', 'Lotaria', 'Raspadinhas One', 'Raspadinhas Two', 'Menu']
    num = write_menu(
        "Eliminar Rank", "\nEscolha um opção para eliminar: ", opcoes)
    if num == 0:
        menu_gestao(user, users)
    else:
        while num > 0 and num < 5:
            todas_linhas = []
            with open('register.txt', 'r') as file:
                todas_linhas = file.readlines()

            with open('register.txt', 'w') as file:
                for linha in todas_linhas:
                    partes = linha.split()
                    if len(partes) >= (num+2) and partes[0] == user.nome:
                        partes[num+2] = "0"
                        nova_linha = " ".join(partes) + "\n"
                        file.write(nova_linha)
                        print(f"Rank {partes[num+2]} Apagado com sucesso!")
                        time.sleep(2)
                    else:
                        file.write(linha)
                break
        else:
            print("Erro! Opção errada!")
            time.sleep(2)
            menu_gestao(user, users)
    menu_gestao(user, users)


'''def delete_rank(user):
    clear()
    escolhas = ['Apagar Rank Quiz', 'Apagar Rank Lotaria', 'Apagar Rank Raspadinhas One', 'Apagar Rank Raspadinhas Two', 'Menu\n']
    num = write_menu("Apagar Rank","Escolha uma Opção: ", escolhas)
    match num:
        case 1: 
            clear()
            delete_rank_quiz(user)
        case 2: 
            clear()
            delete_rank_lot(user)
        case 3: 
            clear()
            delete_rank_rasp1(user)
        case 4: 
            clear()
            delete_rank_rasp2(user)
        case 0:
            clear()
            menu_gestao(user)
        case _: 
            print(erro_invalid)
            menu_gestao(user)

def delete_rank_quiz(user):
    
    write_title("Eliminar Rank Quiz")
    choice = input("Tem a certeza que deseja eliminar o Rank Quiz? Sim/Nao: ")
    if choice == "sim":
        todas_linhas = []
        with open('register.txt', 'r') as file:
            todas_linhas = file.readlines()
            
        with open('register.txt', 'w') as file:  
            for linha in todas_linhas:
                partes = linha.split()
                if len(partes) >= 4 and partes[0] == user.nome:
                    partes[3] = "0"
                    nova_linha = " ".join(partes) + "\n"
                    file.write(nova_linha)
                    print("Rank Quiz Apagado com sucesso!")
                else:
                    file.write(linha)
                    
    elif choice == "nao": 
        menu_gestao(user)
    else: 
        print("Erro! Opção errada!")
        time.sleep(2)
        menu_gestao(user)
    menu_gestao(user)
    
def delete_rank_lot(user):
    
    write_title("Eliminar Rank Lotaria")
    choice = input("Tem a certeza que deseja eliminar o Rank Lotaria? Sim/Nao: ")
    if choice == "sim":
        todas_linhas = []
        with open('register.txt', 'r') as file:
            todas_linhas = file.readlines()
            
        with open('register.txt', 'w') as file:  
            for linha in todas_linhas:
                partes = linha.split()
                if len(partes) >= 5 and partes[0] == user.nome:
                    partes[4] = "0"
                    nova_linha = " ".join(partes) + "\n"
                    file.write(nova_linha)
                    print("Rank Lotaria Apagado com sucesso!")
                else:
                    file.write(linha)
                    
    elif choice == "nao": 
        menu_gestao(user)
    else: 
        print("Erro! Opção errada!")
        time.sleep(2)
        menu_gestao(user)
    menu_gestao(user)

def delete_rank_rasp1(user):
    
    write_title("Eliminar Rank Raspadinhas One")
    choice = input("Tem a certeza que deseja eliminar o Rank Raspadinhas One? Sim/Nao: ")
    if choice == "sim":
        todas_linhas = []
        with open('register.txt', 'r') as file:
            todas_linhas = file.readlines()
            
        with open('register.txt', 'w') as file:  
            for linha in todas_linhas:
                partes = linha.split()
                if len(partes) >= 6 and partes[0] == user.nome:
                    partes[5] = "0"
                    nova_linha = " ".join(partes) + "\n"
                    file.write(nova_linha)
                    print("Rank Raspadinhas One Apagado com sucesso!")
                else:
                    file.write(linha)
                    
    elif choice == "nao": 
        menu_gestao(user)
    else: 
        print("Erro! Opção errada!")
        time.sleep(2)
        menu_gestao(user)
    menu_gestao(user)
    
def delete_rank_rasp2(user):
    
    write_title("Eliminar Rank Raspadinhas Two")
    choice = input("Tem a certeza que deseja eliminar o Rank Raspadinhas Two? Sim/Nao: ")
    if choice == "sim":
        todas_linhas = []
        with open('register.txt', 'r') as file:
            todas_linhas = file.readlines()
            
        with open('register.txt', 'w') as file:  
            for linha in todas_linhas:
                partes = linha.split()
                if len(partes) >= 6 and partes[0] == user.nome:
                    partes[6] = "0"
                    nova_linha = " ".join(partes) + "\n"
                    file.write(nova_linha)
                    print("Rank Raspadinhas Two Apagado com sucesso!")
                else:
                    file.write(linha)
                    
    elif choice == "nao": 
        menu_gestao(user)
    else: 
        print("Erro! Opção errada!")
        time.sleep(2)
        menu_gestao(user)
    menu_gestao(user)'''
