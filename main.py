from utils import menu_functions, db_functions

objetos_palestras, objetos_workshops = db_functions.carregar_todos_eventos()

while True:
    try:
        print("______________ MENU _______________")
        print("_" * 35)
        print("[1] Adicionar evento")
        print("[2] Mostrar eventos")
        print("[3] Fazer inscrição")
        print("[4] Cancelar inscrição")
        print("[5] Relatório")
        print("[0] Sair")
        print('_' * 35)
        escolha = int(input("Escolha uma opção: "))

        match escolha:
            case 1:
                # 1. Adiciona o evento e salva no JSON
                menu_functions.adicionar_evento()
                
                # 2. RECARREGA OS DADOS!
                # Atualiza as variáveis objetos_palestras e objetos_workshops
                objetos_palestras, objetos_workshops = db_functions.carregar_todos_eventos()
                
            case 2:
                menu_functions.mostrar_eventos(objetos_palestras, objetos_workshops)

            case 3:
                menu_functions.fazer_inscricao(objetos_palestras, objetos_workshops)

            case 4:
                menu_functions.cancelar_inscricao()

            case 5:
                menu_functions.relatorios(objetos_palestras, objetos_workshops)


            case 0:
                print("Saindo...")
                break

            case _:
                print("Digite uma opção válida!")

    except ValueError:
        print("Erro! Digite um número inteiro, ou 0 para sair.\n")
        continue