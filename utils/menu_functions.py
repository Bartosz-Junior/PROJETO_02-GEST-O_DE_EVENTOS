# FUNÇÕES RELACIONADAS A MAIN/MENU PRINCIPAL

from utils import helpers_functions

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


def mostrar_eventos(dict_dados):
    while True:
        try:
            print("________ EVENTOS DISPONIVEIS ________")
            print()
            print("Digite [1] TODOS:")
            print("Digite [2] BUSCAR POR:")
            print("Digite [0] VOLTAR:")
            escolha = int(input())

            if escolha == 1:
                helpers_functions.listar_dados(dict_dados["palestras"], "palestras")
                helpers_functions.listar_dados(dict_dados["workshops"], "workshops")

            elif escolha == 2:
                helpers_functions.buscar_eventos(dict_dados)

            elif escolha == 0:
                break

        except ValueError:
            print("Opção inválida!")


def fazer_inscricao(dicts_dados):

    print("________ INSCREVER PARTICIPANTE ________")
    print()
    print("Digite [1] para PALESTRAS:")
    print("Digite [2] para WORKSHOPS:")
    escolha_evento = int(input())

    if escolha_evento == 1:
        helpers_functions.add_participante(dicts_dados["palestras"], "palestras", "database/palestras.json")

    elif escolha_evento == 2:   
        helpers_functions.add_participante(dicts_dados["workshops"], "workshops", "database/workshops.json")
    
    else:
        pass

def buscar_email_cancelamento(dict_dados):
    email = str(input("Escolha o e-mail para realizar o cancelamento da inscrição: "))

    for participante in dict_dados["participantes"]:
        if email == participante["email"]:
            helpers_functions.cancelar_inscricao_participante(participante)
            break
    else:
        print("E-mail não encontrado.") 

def buscar_email_checkin(dict_dados):

    email = str(input("Escolha o e-mail para realizar o check-in: "))

    for participante in dict_dados["participantes"]:

        if email == participante["email"]:
            helpers_functions.fazer_checkin_participante(participante)
            break
    else:
        print("E-mail não encontrado.")

def relatorios(dicts_eventos):
    print("\n===== RELATÓRIOS =====\n")

    # Totais
    total_palestras = len(dicts_eventos["palestras"])
    total_workshops = len(dicts_eventos["workshops"])
    print(f"Total de palestras: {total_palestras}")
    print(f"Total de workshops: {total_workshops}")
    print(f"Total de eventos: {total_palestras + total_workshops}\n")

    # Inscrições por evento
    print(" Inscrições por evento:")
    for evento in dicts_eventos:
        print(f"- {evento["tema"]}: {evento["numero_inscritos"]} inscritos")

    # Total de participantes
    total_participantes = sum(e["numero_inscritos"] for e in dicts_eventos)
    print(f"\nTotal de participantes (contagem geral): {total_participantes}\n")

    # Evento mais popular