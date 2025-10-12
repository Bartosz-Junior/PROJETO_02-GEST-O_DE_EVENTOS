from utils import menu_functions, db_functions

objs_palestras, objs_workshops, objs_participantes = db_functions.carregar_todos_objetos()


while True:
    for p in objs_participantes:
        print(p)

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
                # Adiciona o evento e salva no JSON
                menu_functions.adicionar_evento()
                
                # RECARREGA OS DADOS! apos a adição do evento
                objs_palestras, objs_workshops, objs_participantes = db_functions.carregar_todos_objetos()
                
            case 2:
                menu_functions.mostrar_eventos(objs_palestras, objs_workshops)

            case 3:
                menu_functions.fazer_inscricao(objs_palestras, objs_workshops)

                objs_palestras, objs_workshops, objs_participantes = db_functions.carregar_todos_objetos()

            case 4:
                menu_functions.cancelar_inscricao_participante()

                objs_palestras, objs_workshops, objs_participantes = db_functions.carregar_todos_objetos()

            case 5:
                menu_functions.fazer_checkin_participante(objs_participantes)

                objs_palestras, objs_workshops, objs_participantes = db_functions.carregar_todos_objetos()

            case 6:
                menu_functions.relatorios(objs_palestras, objs_workshops)

            case 0:
                print("Saindo...")
                break

            case _:
                print("Digite uma opção válida!")

    except ValueError:
        print("Erro! Digite um número inteiro, ou 0 para sair.\n")
        continue