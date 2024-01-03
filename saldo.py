import sys
import time
import os

sys.path.append(r'C:\Users\sergi\OneDrive\Documents')
from functions import clear, write_menu, is_valid_name, erro_invalid, write_title


def save_transaction(username, tipo_transacao, quant):
    filename = (f"{username}_saldo.txt")
    with open(filename, 'a') as file:
        if tipo_transacao == 'deposito':
            file.write(f"Dep: +{quant}\n")
        elif tipo_transacao == 'levantamento':
            file.write(f"Lev: -{quant}\n")
            
            
def jogada_lotaria(username, jogada):
    
        filename = (f"{username}_jogada.txt")
        with open(filename, 'a') as file: 
            file.write(f"{jogada}\n")
            
def limpar_conteudo_arquivos_jogada():
    try:
        for filename in os.listdir():
            if filename.endswith("_jogada.txt"):
                with open(filename, 'w') as file:
                    file.truncate(0)  # Limpa o conteúdo do arquivo
                print(f"Conteúdo do arquivo {filename} limpo com sucesso.")
                time.sleep(2)
    except Exception as e:
        print(f"Erro ao limpar conteúdo dos arquivos: {e}")
        time.sleep(2)

def menu_saldo(user, users):
    
    clear()
    opcoes = ['Levantamentos', 'Depósitos', 'Saldo', 'Histórico Transações', 'Sair']
    num = write_menu('Saldo','\nEscolha uma Opção: ', opcoes)
    try: 
        match num:
            case 1: 
                clear()
                todas_linhas = []
                with open('register.txt', 'r') as file:
                    todas_linhas = file.readlines()
                
                with open('register.txt', 'w') as file:  
                    for linha in todas_linhas:
                        partes = linha.split()
                        if len(partes) >= (3) and partes[0] == user.nome:
                            try:
                                levantamento = int(input("Qual a Quantia que deseja levantar?\n"))
                                partes[2] = int(partes[2]) - levantamento
                                partes[2] = str(partes[2])
                            except ValueError:
                                print("Erro! Digite um valor numerário!")                      
                            nova_linha = " ".join(partes) + "\n"
                            file.write(nova_linha)
                            print(f"Saldo Actualizado com sucesso!")
                            time.sleep(2)
                            save_transaction(user.nome, 'levantamento', levantamento)
                            print(f"Historico Actualizado com sucesso!")
                            time.sleep(2)
                        else:
                            file.write(linha)
                menu_saldo(user, users)
                
            case 2: 
                clear()
                todas_linhas = []
                with open('register.txt', 'r') as file:
                    todas_linhas = file.readlines()
                
                with open('register.txt', 'w') as file:  
                    for linha in todas_linhas:
                        partes = linha.split()
                        if len(partes) >= (3) and partes[0] == user.nome:
                            try:
                                deposito = int(input("Qual a Quantia que deseja Depositar?\n"))
                                partes[2] = int(partes[2]) + deposito
                                partes[2] = str(partes[2])
                            except ValueError:
                                print("Erro! Digite um valor numerário!")                      
                            nova_linha = " ".join(partes) + "\n"
                            file.write(nova_linha)
                            print(f"Saldo Actualizado com sucesso!")
                            time.sleep(2)
                            save_transaction(user.nome, 'deposito', deposito)
                            print(f"Historico Actualizado com sucesso!")
                            time.sleep(2)
                        else:
                            file.write(linha)
                menu_saldo(user, users)
                
            case 3: 
                clear()
                todas_linhas = []
                with open('register.txt', 'r') as file:
                    todas_linhas = file.readlines()
                    
                for linha in todas_linhas:
                    partes = linha.split() 
                    if partes[0] == user.nome:
                        status = True    
                        while status == True:      
                            write_title("Saldo")
                            print(f"Usuário: {user.nome}\n")
                            print(f"Saldo: {partes[2]}€\nTokens: {partes[7]}")
                            op = input("\nClick em qualquer tecla para sair!")
                            if op != None:
                                status == False
                                break
                    else:
                        print("Erro! User não encontrado!")
                clear()
                menu_saldo(user, users)
            
            case 4:
                clear()
                filename = f"{user.nome}_saldo.txt"
                try:
                    with open(filename, 'r') as file:
                        transacoes = file.readlines()
                        write_title(f'Histórico {user.nome}')
                        for transacao in transacoes:
                            print(transacao.strip())
                except FileNotFoundError:    
                    print("Erro! Ficheiro não encontrado!")    
                op = input("\nClick em qualquer tecla para sair!")
                if op != None:
                    menu_saldo(user, users)
                
                clear()
                menu_saldo(user, users)
            
            case 0:
                clear()
                from menu import menu_principal
                menu_principal(user, users)
        
    except ValueError:
        erro_invalid()
        menu_saldo(user, users)