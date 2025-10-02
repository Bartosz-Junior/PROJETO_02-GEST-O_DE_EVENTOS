from utils import functions
from eventos.palestra import Palestra
from eventos.workshop import Workshop
from eventos.workshop import Evento
from utils import functions
import os

DIRETORIO_PALESTRAS = 'database/palestras.json'
DIRETORIO_WORKSHOPS = 'database/wokshops.json'
DIRETORIO_PARTICIPANTES = "database/participantes.json"

# CARREGA OS DADOS DO JSON E A VARIAVEL RECEBER UM DICT
palestras = functions.carregar_json(DIRETORIO_PALESTRAS)
workshops = functions.carregar_json(DIRETORIO_WORKSHOPS)

#print(palestras)
print(workshops)

objetos_palestras = functions.carregar_instancias(palestras, Palestra)
objetos_workshops = functions.carregar_instancias(workshops, Workshop)

while True:
    try:
        print("_" * 35)
        print("[1] Adicionar EVENTO")
        print("[2] Mostrar EVENTOS")
        print("[3] Fazer inscrição")
        print("[4] Cancelar inscrição")
        print("[5] Buscar Evento")
        print("[6] pass")
        print("[7] pass")
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
                        print("[1] para PALESTRAS:")
                        print("[2] para WORKSHOPS:")
                        print("[3] para TODOS:")
                        print("[0] para VOLTAR:")
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
                escolha_evento = int(input("[1] palestras, [2] workshops"))
                if escolha_evento == 1:
                    functions.add_participante(objetos_palestras) 

                elif escolha_evento == 2:   
                    functions.add_participante(objetos_workshops)

                else:
                    pass           

            case 4:
                pass

            case 5:
                while True:
                    try:
                        print("__________ BUSCAR EVENTO __________" )
                        print("[1] Buscar por Data(dd/mm/aaaa):")
                        print("[2] Buscar por Categria(Ex.: Tech):")
                        print("[0] para VOLTAR:")
                        escolha = int(input())

                        if escolha == 1:
                            functions.buscar_evento_data()

                        if escolha == 2:
                            functions.buscar_evento_categoria()

                        elif escolha == 0:
                            break
                    except ValueError:
                        print("Opção inválida!")

            case 6:
                pass

            case 0:
                print("Saindo...")
                break

            case _:
                print("Digite uma opção válida!!")

    except ValueError:
        print("Erro! Digite um número inteiro, ou 0 para sair.\n")
        continue