from utils import menu_functions, db_functions

while True:

    dict_dados = db_functions.carregar_dict_dados()

    try:
        print("______________ MENU _______________")
        print("_" * 35)
        print("[1] Adicionar evento")
        print("[2] Mostrar eventos")
        print("[3] Fazer inscrição")
        print("[4] Cancelar inscrição")
        print("[5] Fazer check-in do participante")
        print("[6] Relatório")
        print("[0] Sair")
        print('_' * 35)
        escolha = int(input("Escolha uma opção: "))

        match escolha:
            case 1:
                menu_functions.adicionar_evento()
                
            case 2:
                menu_functions.mostrar_eventos(dict_dados)

            case 3:
                menu_functions.fazer_inscricao(dict_dados)

            case 4:
                menu_functions.buscar_email_cancelamento(dict_dados)

            case 5:
                menu_functions.buscar_email_checkin(dict_dados)

            case 6:
                menu_functions.relatorios(dict_dados)

            case 0:
                print("Saindo...")
                break

            case _:
                print("Digite uma opção válida!")

    except ValueError:
        print("Erro! Digite um número inteiro, ou 0 para sair.\n")
        continue