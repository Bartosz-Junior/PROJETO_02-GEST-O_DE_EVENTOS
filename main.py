import cad_eventos as evento

while True:
    try:
        print("*" * 35)
        print("[1] Adicionar PALESTRA")
        print("[2] Adicionar WORKSHOP")
        print("[3] Fazer inscrição")
        print("[4] Cancelar inscrição")
        print("[5] Listar Palestras")
        print("[6] Listar Workshops")
        print("[7] Listar todos os eventos")
        print("[0] Sair")
        print('*' * 35)

        # Entrada do usuário para escolha da opção
        escolha = int(input("Escolha uma opção: "))

        match escolha:
            case 1:
                palestra = evento.Palestra()
                palestra.add_palestra()
            case 2:
                workshop = evento.Workshop()
                workshop.add_workshop()
            case 3:
                pass
            case 4:
                pass
            case 5:
                palestra.listar_palestras()
            case 6:
                workshop.listar_workshop()

    except ValueError:
        print("Erro! Digite um número inteiro, ou 0 para sair.\n")
        continue
