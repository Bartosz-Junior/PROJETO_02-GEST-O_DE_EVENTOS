# FUNÇÕES AUXILIARES

from eventos.palestra import Palestra
from eventos.workshop import Workshop
from eventos.participantes import Participante
from datetime import datetime
import json, os, datetime


def add_palestra():
    hoje = datetime.date.today()
    try:                            
        print("__________ Adicionar Palestra __________" )

        nome = str(input("Tema da palestra: "))

        while True:
            data_evento = str(input("Data de realização dd/mm/aaaa:"))
            data_formatada = datetime.datetime.strptime(data_evento, "%d/%m/%Y")

            if data_formatada < hoje:
                print("A data do evento não pode ser menor que a data atual!")
                continue
            else:
                break

        local_evento = str(input("Local: "))
        
        while True:
            capacidade_max = int(input("Capacidade de pessoas: "))
            if capacidade_max <= 0:
                print("O evento deve comportar um número maior que zero de pessoas.")
                continue
            else:
                break

        categoria = str(input("Categoria [Tech/Marketing]: ")).lower().strip()
        numero_inscritos = 0

        while True:
            preco_ingresso = float(input("Preço da entrada: "))
            if preco_ingresso < 0:
                print("O preço não pode ser negativo.")
                continue
            else:
                break

        
        nova_palestra = Palestra(nome, data_formatada, local_evento, capacidade_max, categoria, numero_inscritos, preco_ingresso)

        nova_palestra.listar_eventos()

    except ValueError:
        print("Opção inválida!")


def add_workshop():
    hoje = datetime.date.today()
    try:                            
        print("__________ Adicionar workshop __________" )

        nome = str(input("Tema do workshop: "))

        while True:
            data_evento = str(input("Data de realização dd/mm/aaaa:"))
            data_formatada = datetime.datetime.strptime(data_evento, "%d/%m/%Y")

            if data_formatada < hoje:
                print("A data do evento não pode ser menor que a data atual!")
                continue
            else:
                break

        local_evento = str(input("Local: "))
        
        while True:
            capacidade_max = int(input("Capacidade de pessoas: "))
            if capacidade_max <= 0:
                print("O evento deve comportar um número maior que zero de pessoas.")
                continue
            else:
                break

        categoria = str(input("Categoria [Tech/Marketing]: ")).lower().strip()
        numero_inscritos = 0

        while True:
            preco_ingresso = float(input("Preço da entrada: "))
            if preco_ingresso < 0:
                print("O preço não pode ser negativo.")
                continue
            else:
                break

        
        novo_workshop = Workshop(nome, data_formatada, local_evento, capacidade_max, categoria, numero_inscritos, preco_ingresso)

        novo_workshop.listar_eventos()

    except ValueError:
        print("Opção inválida!")


def listar_objetos(objetos, tipo):
    print("\n" + "="*30)
    print(f"      LISTA DE {tipo}")
    print("="*30)

    if not objetos:
        print(f"Nenhum evento cadastrado ainda.")
        return

    for i, objeto in enumerate(objetos):
        print(f"\n--- {tipo} {i} ---")
        print(objeto)

    print("\n" + "="*30)

# def listar_palestras(objeto):
#     print("\n" + "="*30)
#     print("      LISTA DE PALESTRAS")
#     print("="*30)

#     if not objeto:
#         print("Nenhuma palestra cadastrado ainda.")
#         return

#     for i, evento in enumerate(objeto):
#         print(f"\n--- Palestra {i} ---")
#         print(evento)

#     print("\n" + "="*30)


# def listar_workshops(objeto):
#     print("\n" + "="*30)
#     print("      LISTA DE WORKSHOPS")
#     print("="*30)

#     if not objeto:
#         print("Nenhum workshop cadastrado ainda.")
#         return

#     for i, evento in enumerate(objeto):
#         print(f"\n--- Workshop {i} ---")
#         print(evento)

#     print("\n" + "="*30)


def add_participante(evento, tipo):
    try:
        if not evento:
            print("Nenhum evento disponível.")
            return

        # Chama a função para listar
        listar_objetos(evento, tipo)
        indice = int(input("Informe qual evento deseja participar: "))

        if (indice < 0) or (indice >= len(evento)):
            print("Evento inválido!")
            return
        
        nome = str(input("Informe o nome: ")).upper()
        email = str(input("Informe o e-mail: ")).lower()
        evento_escolhido = evento[indice]
        
        if nome and email and evento_escolhido:
            participante = Participante(nome, email, evento_escolhido.nome)
            print(participante)

            dados_participante = {
                "Nome:": participante.nome,
                "E-mail": participante.email,
                "Evento escolhido": participante.evento
            }

            participante.salvar_participante(dados_participante, evento_escolhido)

    except ValueError:
        print("Dados informados inválidos")

    except IndexError:
        print("Evento inválido! O número do evento não existe na lista.")

    except FileNotFoundError:
        # Se o arquivo não existir, inicia a lista vazia
        carrega_participantes = []

    except json.JSONDecodeError:
        # Se o arquivo estiver vazio/inválido, inicia a lista vazia e avisa
        print("Aviso: Arquivo de participantes inválido ou vazio. Iniciando nova lista.")
        carrega_participantes = []


def buscar_evento_data():
    with open("database\palestras.json", "r", encoding="utf-8") as file:
        carrega_palestras = json.load(file)

    with open("database\wokshops.json", "r", encoding="utf-8") as file:
        carrega_workshops = json.load(file)

        data_busca = str(input("Informe a data do evento (dd/mm/aaaa): "))

        for i, v in enumerate(carrega_palestras):
            if v["Data"] == data_busca:
                print(f"_____ PALESTRA {i + 1} _____")
                print(f"Tema: {v["Tema"]:5}")
                print(f"Data: {v["Data"]:5}")
                print(f"Local: {v["Local"]:5}")
                print(f"Capacidade: {v["Capacidade_max"]:5}")
                print(f"Categoria: {v["Categoria"]:5}")
                print(f"Preço: R${v["Preço ingresso"]:5.2f}\n")

        for i, v in enumerate(carrega_workshops):
            if v["Data"] == data_busca:
                print(f"_____ WORKOSHOP {i + 1} _____")
                print(f"Tema: {v["Tema"]:5}")
                print(f"Data: {v["Data"]:5}") 
                print(f"Local: {v["Local"]:5}")
                print(f"Capacidade: {v["Capacidade_max"]:5}")
                print(f"Categoria: {v["Categoria"]:5}")
                print(f"Preço: R${v["Preço ingresso"]:5.2f}\n")

def buscar_evento_categoria():
    with open("database\palestras.json", "r", encoding="utf-8") as file:
        carrega_palestras = json.load(file)

    with open("database\wokshops.json", "r", encoding="utf-8") as file:
        carrega_workshops = json.load(file)

        categoria_busca = str(input("Informe a categoria do evento:")).lower().strip()

        for i, v in enumerate(carrega_palestras):
            if v["Categoria"] == categoria_busca:
                print(f"_____ PALESTRA {i + 1} _____")
                print(f"Tema: {v["Tema"]:5}")
                print(f"Data: {v["Data"]:5}")
                print(f"Local: {v["Local"]:5}")
                print(f"Capacidade: {v["Capacidade_max"]:5}")
                print(f"Categoria: {v["Categoria"]:5}")
                print(f"Preço: R${v["Preço ingresso"]:5.2f}\n")

        for i, v in enumerate(carrega_workshops):
            if v["Categoria"] == categoria_busca:
                print(f"_____ WORKOSHOP {i + 1} _____")
                print(f"Tema: {v["Tema"]:5}")
                print(f"Data: {v["Data"]:5}") 
                print(f"Local: {v["Local"]:5}")
                print(f"Capacidade: {v["Capacidade_max"]:5}")
                print(f"Categoria: {v["Categoria"]:5}")
                print(f"Preço: R${v["Preço ingresso"]:5.2f}\n")