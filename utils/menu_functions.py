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


def mostrar_eventos(dicts_palestras, dicts_workshops):
    while True:
        try:
            print("________ EVENTOS DISPONIVEIS ________")
            print()
            print("Digite [1] TODOS:")
            print("Digite [2] BUSCAR POR:")
            print("Digite [0] VOLTAR:")
            escolha = int(input())

            if escolha == 1:
                helpers_functions.listar_dados(dicts_palestras, "palestras")
                helpers_functions.listar_dados(dicts_workshops, "workshops")

            elif escolha == 2:
                todos_eventos = dicts_palestras + dicts_workshops  # juntar tudo
                helpers_functions.buscar_eventos(todos_eventos)
            
            elif escolha == 0:
                break

        except ValueError:
            print("Opção inválida!")


def fazer_inscricao(dicts_palestras, dicts_workshops):

    print("________ INSCREVER PARTICIPANTE ________")
    print()
    print("Digite [1] para PALESTRAS:")
    print("Digite [2] para WORKSHOPS:")
    escolha_evento = int(input())

    if escolha_evento == 1:
        helpers_functions.add_participante(dicts_palestras, "PALESTRAS", "database/palestras.json")

    elif escolha_evento == 2:   
        helpers_functions.add_participante(dicts_workshops, "WORKSHOPS", "database/workshops.json")
    
    else:
        pass

def cancelar_inscricao_participante(dicts_participantes, dicts_palestras, dicts_workshops):
    email = str(input("Escolha o e-mail para realizar o cancelamento da inscrição: "))

    for participante in dicts_participantes:
        if email == participante.email:
            evento_remover = participante.remover_inscrito()

            for evento in (dicts_palestras + dicts_workshops):
                if evento.tema == evento_remover:
                    evento.reduzir_numero_inscritos()
                    break
            
            else:
                    print("Evento não encontrado")

def buscar_email_participante(dicts_participantes):

    email = str(input("Escolha o e-mail para realizar o check-in: "))

    for participante in dicts_participantes:

        if email == participante["email"]:
            helpers_functions.fazer_checkin_participante(participante)
            break

        print("E-mail não encontrado.")

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
        print(f"- {evento.tema}: {evento.numero_inscritos} inscritos")

    # Total de participantes
    total_participantes = sum(e.numero_inscritos for e in palestras + workshops)
    print(f"\nTotal de participantes (contagem geral): {total_participantes}\n")

    # Evento mais popular
    if palestras + workshops:
        mais_popular = max(palestras + workshops, key=lambda e: e.numero_inscritos)
        if mais_popular.numero_inscritos > 0:
            print(f" Evento mais popular: {mais_popular.tema} ({mais_popular.numero_inscritos} inscritos)")
        else:
            print("Nenhum evento tem inscritos ainda.")
    else:
        print("Nenhum evento cadastrado.")

