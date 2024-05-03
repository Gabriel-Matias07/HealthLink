import formulario_cartao

def opcoes_pagamento():
    print("Escolha uma opção de pagamento:")
    print("1 - Cartão de crédito")
    print("2 - Cartão de débito")
    print("3 - PIX")
    
    opcao = input("Opção: ")
    
    match opcao:
        case '1':
            formulario_cartao.main()
        case '2':
            print("Pagamento por cartão de débito.")
        case '3':
            print("Pagamento via PIX.")
        case _:
            print("Opção inválida.")

opcoes_pagamento()