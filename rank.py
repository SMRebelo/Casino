import sys
import time
import os

sys.path.append(r'C:\Users\sergi\OneDrive\Documents')
from functions import clear, write_menu, is_valid_name, erro_invalid, write_title, read_users, print_users

def menu_rank(user, users):
    from menu import menu_principal
    clear()
    opcoes = ['Rank Quiz', 'Rank Lotaria', 'Rank Raspadinhas One', 'Rank Raspadinhas Two', 'Sair']
    try:
        num = write_menu('Rank','\nEscolha uma Opção: ', opcoes)
        if num == 0:
            menu_principal(user, users)
        else:
            status = True
            while status == True: 
                clear()           
                write_title(f'{opcoes[num-1]}')
                usuarios = read_users()
                top = {} 
 
                names = ['score_quiz', 'score_lot', 'score_rasp1', 'score_rasp2']    
                for user in usuarios:
                    escolha = getattr(user, names[num-1], None)
                    top[user.nome] = int(escolha)
                      
                top_sorted = dict(sorted(top.items(), key=lambda item: item[1], reverse=True))
                for name in top_sorted:
                    print(f"{name}: {top_sorted[name]}")
                    
                op = input("\nClick Enter para sair!")
                if op != None:
                    status = False
                    clear()
                    menu_rank(user, users)
            else:
                print("Erro! Opção inválida!")
                time.sleep(2)
                menu_rank(user, users)
    except ValueError:
        print("Erro! Opção Inválida!")
        time.sleep(2)
        menu_rank(user, users)

    

            

