# FUNÇÕES AUXILIARES

from utils import db_functions
from eventos.palestra import Palestra
from eventos.workshop import Workshop
from eventos.participantes import Participante
from datetime import datetime
import json, os, datetime


def add_evento(tipo_evento):
    hoje = datetime.datetime.today()
    try:                            
        print("__________ Adicionar Palestra __________")

        tema = str(input("Tema: "))

        while True:
            try:
                data = input("Data de realização (dd/mm/aaaa): ")
                # tenta converter
                data_formatada = datetime.datetime.strptime(data, "%d/%m/%Y")      
                # valida se é no passado
                if data_formatada < hoje:
                    print("A data do evento não pode ser menor que a data atual!")
                    continue 
                # se tudo certo, sai do loop
                break

            except ValueError:
                print("Formato inválido! Digite a data no formato dd/mm/aaaa.\n")
                continue

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

        if tipo_evento == "palestra":
            novo_evento = Palestra(tema, data, local_evento, capacidade_max, numero_inscritos, categoria, preco_ingresso)

            dados = db_functions.carregar_json("database/palestras.json")
            dados.append(novo_evento.gerar_dict())
            db_functions.salvar_json("database/palestras.json", dados)


        elif tipo_evento == "workshop":
            novo_evento = Workshop(tema, data, local_evento, capacidade_max, numero_inscritos, categoria, preco_ingresso)

            dados = db_functions.carregar_json("database/workshops.json")
            dados.append(novo_evento.gerar_dict())
            db_functions.salvar_json("database/workshops.json", dados)


        print("Evento cadastrado com sucesso!")

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


def add_participante(evento, tipo):
    try:
        if not evento:
            print("Nenhum evento disponível.")
            return

        listar_objetos(evento, tipo)
        indice = int(input("Informe qual evento deseja participar: "))

        if (indice < 0) or (indice >= len(evento)):
            print("Evento inválido!")
            return
        
        nome = str(input("Informe o nome do participante: ")).upper()
        email = str(input("Informe o e-mail do particante: ")).lower()
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
    with open("database/palestras.json", "r", encoding="utf-8") as file:
        carrega_palestras = json.load(file)

    with open("database/workshops.json", "r", encoding="utf-8") as file:
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
    with open("database/palestras.json", "r", encoding="utf-8") as file:
        carrega_palestras = json.load(file)

    with open("database/workshops.json", "r", encoding="utf-8") as file:
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
                print(f"_____ WORKSHOP {i + 1} _____")
                print(f"Tema: {v["Tema"]:5}")
                print(f"Data: {v["Data"]:5}") 
                print(f"Local: {v["Local"]:5}")
                print(f"Capacidade: {v["Capacidade_max"]:5}")
                print(f"Categoria: {v["Categoria"]:5}")
                print(f"Preço: R${v["Preço ingresso"]:5.2f}\n")