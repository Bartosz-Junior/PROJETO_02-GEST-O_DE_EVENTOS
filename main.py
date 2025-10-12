from utils import menu_functions, db_functions



while True:

    objs_palestras, objs_workshops, objs_participantes = db_functions.carregar_todos_objetos()

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
                
            case 2:
                menu_functions.mostrar_eventos(objs_palestras, objs_workshops)

            case 3:
                menu_functions.fazer_inscricao(objs_palestras, objs_workshops)

            case 4:
                menu_functions.cancelar_inscricao_participante(objs_participantes, objs_palestras, objs_workshops)

            case 5:
                menu_functions.fazer_checkin_participante(objs_participantes)

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