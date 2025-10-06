# FUNÇÕES RELACIONADAS A MAIN/MENU PRINCIPAL

from utils import helpers_functions
from datetime import datetime


def adicionar_evento():
    while True:
        try:
            print("__________ ADICIONAR EVENTO __________")
            print()
            print("Digite [1] para PALESTRAS:")
            print("Digite [2] para WORKSHOPS:")
            print("Digite [0] para VOLTAR:")
            escolha = int(input())

            if escolha == 1:
                helpers_functions.add_evento("palestra")

            elif escolha == 2:
                helpers_functions.add_evento("workshop")

            elif escolha == 0:
                break

        except ValueError:
            print("Opção inválida!")


def mostrar_eventos(obj_palestras, obj_workshops):
    while True:
        try:
            print("________ EVENTOS DISPONIVEIS ________")
            print()
            print("Digite [1] TODOS:")
            print("Digite [2] BUSCAR POR:")
            print("Digite [0] VOLTAR:")
            escolha = int(input())

            if escolha == 1:
                helpers_functions.listar_objetos(obj_palestras, "PALESTRAS")
                helpers_functions.listar_objetos(obj_workshops, "WORKSHOPS")

            elif escolha == 2:
                todos_eventos = obj_palestras + obj_workshops  # juntar tudo
                helpers_functions.buscar_eventos(todos_eventos)
            
            elif escolha == 0:
                break

        except ValueError:
            print("Opção inválida!")


def fazer_inscricao(obj_palestras, obj_workshops):

    print("________ INSCREVER PARTICIPANTE ________")
    print()
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

def relatorios(palestras, workshops):
    print("\n===== RELATÓRIOS =====\n")

    # Totais
    total_palestras = len(palestras)
    total_workshops = len(workshops)
    print(f"Total de palestras: {total_palestras}")
    print(f"Total de workshops: {total_workshops}")
    print(f"Total de eventos: {total_palestras + total_workshops}\n")

    # Inscrições por evento
    print(" Inscrições por evento:")
    for evento in palestras + workshops:
        print(f"- {evento.nome}: {evento.numero_inscritos} inscritos")

    # Total de participantes
    total_participantes = sum(e.numero_inscritos for e in palestras + workshops)
    print(f"\nTotal de participantes (contagem geral): {total_participantes}\n")

    # Evento mais popular
    if palestras + workshops:
        mais_popular = max(palestras + workshops, key=lambda e: e.numero_inscritos)
        if mais_popular.numero_inscritos > 0:
            print(f" Evento mais popular: {mais_popular.nome} ({mais_popular.numero_inscritos} inscritos)")
        else:
            print("Nenhum evento tem inscritos ainda.")
    else:
        print("Nenhum evento cadastrado.")

