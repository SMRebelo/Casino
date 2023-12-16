import sys
import time

sys.path.append(r'C:\Users\sergi\OneDrive\Documents')
from functions import clear, write_menu, is_valid_name, erro_invalid, write_title

def menu_principal(user, users):

    clear()
    while True:
        options = ['Quiz','Lotaria','Raspadinhas', 'Saldo', 'Rank', 'Conta', 'Sair']
        opcao = write_menu("CASINO","\nEscolha uma Opção: ", options)
        
        from gestao import menu_gestao # Importar a função diretamente aqui para evitar "incular import" entre ficheiros diferentes
        from saldo import menu_saldo
        from rank import menu_rank
        from lotaria import menu_lotaria
   
        match opcao:
            case 2:
                menu_lotaria(user, users)
            case 4: 
                menu_saldo(user, users)
            case 5:
                menu_rank(user, users)
            case 6:
                menu_gestao(user, users)
            case 0:
                print("Obrigado por visitar o Casino!")
                sys.exit(1)
                        
        time.sleep(4)
    
    
