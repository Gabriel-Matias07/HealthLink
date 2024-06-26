import login
import cadastro
import os
from profissionais import login_prof
from profissionais import cadastro_profissionais

def main():
    print("----Bem vindo ao HealthLink----")
    print("----Digite 1 para Usuário, 2 para Profissional ou 0 para encerrar----")
    user_or_prof = input()
    
    if user_or_prof == '1':
        print("Opção 'Usuário' selecionada! \n")
        print("----Selecione 1 para login, 2 para cadastro ou 0 para encerrar----")
        resposta = input()

        if resposta == '1':
            os.system('cls' if os.name == 'nt' else 'clear')
            login.login_usuario()
        elif resposta == '2':
            os.system('cls' if os.name == 'nt' else 'clear')
            cadastro.introduzir_dados_usuarios()
        elif resposta == '0':
            print('----Fim----')

            return None
        else:
            print("Resposta inválida")
            main()
    elif user_or_prof == '2':
        print("Opção 'Profissional' selecionada! \n")
        print("----Selecione 1 para login, 2 para cadastro ou 0 para encerrar----")
        resposta = input()
        if resposta == '1':
            os.system('cls' if os.name == 'nt' else 'clear')
            login_prof.login_profissional()
        elif resposta == '2':
            os.system('cls' if os.name == 'nt' else 'clear')
            cadastro_profissionais.introduzir_dados_profissional()
        elif resposta == '0':
            print('----Fim----')

            return None
        else:
            print("Resposta inválida")
            main()
    elif user_or_prof == '0':
        print('----Fim----')

        return None
    else:
        print("Resposta inválida")
        main()

if __name__ == "__main__":
    main()