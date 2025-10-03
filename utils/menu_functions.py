# FUNÇÕES RELACIONADAS A MAIN/MENU PRINCIPAL

from utils import helpers_functions
from eventos.palestra import Palestra
from eventos.workshop import Workshop
from eventos.participantes import Participante


def adicionar_evento():
    while True:
        try:
            print("__________ ADICIONAR EVENTO __________")
            print("Digite [1] para PALESTRAS:")
            print("Digite [2] para WORKSHOPS:")
            print("Digite [0] para VOLTAR:")
            escolha = int(input())

            if escolha == 1:
                helpers_functions.add_palestra()

            elif escolha == 2:
                helpers_functions.add_workshop()

            elif escolha == 0:
                break

        except ValueError:
            print("Opção inválida!")

def mostrar_eventos(obj_palestras, obj_workshops):
    while True:
        try:
            print("________ EVENTOS DISPONIVEIS ________")
            print("Digite [1] PALESTRAS:")
            print("Digite [2] WORKSHOPS:")
            print("Digite [3] BUSCAR POR:")
            print("Digite [4] TODOS:")
            print("Digite [0] VOLTAR:")
            escolha = int(input())

            if escolha == 1:
                helpers_functions.listar_objetos(obj_palestras, "PALESTRAS")

            elif escolha == 2:
                helpers_functions.listar_objetos(obj_workshops, "WORKSHOPS")

            elif escolha == 3:
                while True:
                    try:
                        print("______ BUSCAR EVENTO ______")
                        print("Digite [1] Buscar por Data(dd/mm/aaaa):")
                        print("Digite [2] Buscar por Categoria(Ex.: Tech):")
                        print("Digite [0] para VOLTAR:")
                        escolha = int(input())

                        if escolha == 1:
                            helpers_functions.buscar_evento_data()

                        if escolha == 2:
                            helpers_functions.buscar_evento_categoria()

                        elif escolha == 0:
                            break
                    except ValueError:
                        print("Opção inválida!")

            elif escolha == 4:
                helpers_functions.listar_objetos(obj_palestras, "PALESTRAS")
                helpers_functions.listar_objetos(obj_workshops, "WORKSHOPS")

            elif escolha == 0:
                break

        except ValueError:
            print("Opção inválida!")

def fazer_inscricao(obj_palestras, obj_workshops):

    print("________ INSCREVER PARTICIPANTE ________")
    print("Digite [1] para PALESTRAS:")
    print("Digite [2] para WORKSHOPS:")
    escolha_evento = int(input())

    if escolha_evento == 1:
        helpers_functions.add_participante(obj_palestras, "PALESTRAS")

    elif escolha_evento == 2:   
        helpers_functions.add_participante(obj_workshops, "WORKSHOPS")
    
    else:
        pass

def cancelar_inscricao():
    pass

def relatorios():
    print("________ RELATÓRIOS ________")
    pass