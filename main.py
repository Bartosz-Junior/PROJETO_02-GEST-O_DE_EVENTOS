from eventos.palestra import Palestra
from eventos.workshop import Workshop
from eventos.workshop import Evento
import os

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
                while True:
                    try:
                        print("__________ ADICIONAR EVENTO __________" )
                        print("Digte [1] para PALESTRAS:")
                        print("Digte [2] para WORKSHOPS:")
                        print("Digte [0] para VOLTAR:")
                        escolha = int(input())
                        if escolha == 1:
                            palestra.add_evento()
                        elif escolha == 2:
                            workshop.add_evento()
                        elif escolha == 0:
                            break
                    except ValueError:
                        print("Opção inválida!")
                
            case 2:
                while True:
                    try:
                        print("__________ EVENTOS DISPONIVEIS __________" )
                        print("Digte [1] para PALESTRAS:")
                        print("Digte [2] para WORKSHOPS:")
                        print("Digte [3] para TODOS:")
                        print("Digte [0] para VOLTAR:")
                        escolha = int(input())
                        if escolha == 1:
                            palestra.listar_palestras()
                        elif escolha == 2:
                            workshop.listar_workshop()
                        elif escolha == 3:
                            palestra.listar_palestras()
                            workshop.listar_workshop()
                        elif escolha == 0:
                            break
                    except ValueError:
                        print("Opção inválida!")
            case 3:
                pass                

            case 4:
                pass

            case 5:
                pass

            case 6:
                pass

            case 0:
                print("Saindo...")
                break

    except ValueError:
        print("Erro! Digite um número inteiro, ou 0 para sair.\n")
        continue