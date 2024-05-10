import sqlite3

def pegar_informacoes():

    print("--Digite seu telefone--")
    telefone = int(input())
    print("--Digite seu endereço--")
    endereco = str(input())
    print("--Digite sua data de nascimento separado por '-'. Exemplo: '17-09-2003'")
    data_nascimento = str(input())
    print("--Digite seu gênero--")
    genero = str(input())

    print("Informações: \n")
    print(f"Telefone: {telefone}\n Endereço: {endereco}\n Data de Nascimento: {data_nascimento}\n Gênero: {genero}\n")
    print("Deseja alterar alguma informação? S = Sim, N = Não")
    alteracao = str(input())

    # Condição de alteração
    
    if 'S' in alteracao:
        print("\n")
        print("1 - Telefone\n 2 - Endereço\n 3 - Data de Nascimento\n 4 - Gênero\n")
        selecao_campo = str(input())
        if selecao_campo == '1':
            telefone = int(input("Digite o seu telefone: "))
        elif selecao_campo == '2':
            endereco = str(input("Digite o seu endereço: "))
        elif selecao_campo == '3':
            data_nascimento = str(input("Digite sua data de nascimento: "))
        elif genero == '4':
            str(input("Digite seu gênero: "))
    elif 'N' in alteracao:
        print("Cadastro realizado com sucesso")
        #Jogar informações no banco de dados
        #armazenar()
        pass
    else:
        return 'Inválido', None
    
    print("Alteração feita com sucesso!\n")
    print(f"Telefone: {telefone}\n Endereço: {endereco}\n Data de Nascimento: {data_nascimento}\n Gênero: {genero}\n")
    #armazenar()
pegar_informacoes()

#Função para armazenar dados no banco de dados

def armazenar():
    sqlite3.connect("data_user_cadastro.db")