from utils import menu_functions, db_functions

obj_palestras, obj_workshops, obj_participantes = db_functions.carregar_todos_objetos()

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
                # Adiciona o evento e salva no JSON
                menu_functions.adicionar_evento()
                
                # RECARREGA OS DADOS! apos a adição do evento
                obj_palestras, obj_workshops, obj_participantes = db_functions.carregar_todos_objetos()
                
            case 2:
                menu_functions.mostrar_eventos(obj_palestras, obj_workshops)

            case 3:
                menu_functions.fazer_inscricao(obj_palestras, obj_workshops)

                obj_palestras, obj_workshops, obj_participantes = db_functions.carregar_todos_objetos()

            case 4:
                menu_functions.cancelar_inscricao()

            case 5:
                menu_functions.relatorios(obj_palestras, obj_workshops)

            case 0:
                print("Saindo...")
                break

            case _:
                print("Digite uma opção válida!")

    except ValueError:
        print("Erro! Digite um número inteiro, ou 0 para sair.\n")
        continue