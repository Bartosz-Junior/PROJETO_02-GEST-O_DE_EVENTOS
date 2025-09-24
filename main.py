from eventos.palestra import Palestra
from eventos.workshop import Workshop
from eventos.workshop import Evento

while True:
    try:
        print("_" * 35)
        print("[1] Adicionar EVENTO")
        print("[2] Mostrar EVENTOS")
        print("[3] Fazer inscrição")
        print("[4] Cancelar inscrição")
        print("[5] Listar Palestras")
        print("[6] Listar Workshops")
        print("[7] Listar todos os eventos")
        print("[0] Sair")
        print('_' * 35)

        # Entrada do usuário para escolha da opção
        escolha = int(input("Escolha uma opção: "))
        palestra = Palestra()
        workshop = Workshop()
        evento = Evento()

        match escolha:
            case 1:
                evento.add_evento()

            case 2:
                evento.listar_eventos()

            case 3:
                pass                

            case 4:
                pass

            case 5:
                palestra.listar_palestras()

            case 6:
                workshop.listar_workshop()

            case 0:
                print("Saindo...")
                break

    except ValueError:
        print("Erro! Digite um número inteiro, ou 0 para sair.\n")
        continue