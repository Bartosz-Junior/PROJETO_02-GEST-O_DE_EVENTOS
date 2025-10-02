import json, datetime

# funções auxiliares

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

# FUNÇÕES AUXILIARES

from eventos.palestra import Palestra
from eventos.workshop import Workshop
from eventos.participantes import Participante

# from eventos.participante import Participante
from datetime import datetime
import json
import os # para verificar se o arquivo json existe


# TENTA CARREGAR QUALQUER LISTA DE UM ARQUIVO JSON E RETORNA UM DICT
def carregar_json(arquivo):

    if not os.path.exists(arquivo):
        return []

    try:
        with open(arquivo, "r", encoding="utf-8") as file:
            dados = json.load(file)
            return dados

    except json.JSONDecodeError:
        print(f"Erro ao decodificar JSON do arquivo '{arquivo}'")
        return []
    
    except Exception as e:
        print(f"Erro inesperado: {e}")
        return []


def carregar_instancias(dados, instancia_evento):

    eventos = []
    for d in dados:
        # recria objeto Palestra
        p = instancia_evento(
            d["Tema"],
            d["Data"],
            d["Local"],
            d["Capacidade_max"],
            d["Numero_inscritos"],
            d["Categoria"],
            d["Preço ingresso"]
        )
        eventos.append(p)

    return eventos

# def carregar_instancias(dados):

#     workshop = []

#     for d in dados:
#         # recria objeto Palestra
#         w = Workshop(
#             d["Tema"],
#             d["Data"],
#             d["Local"],
#             d["Capacidade_max"],
#             d["Numero_inscritos"],
#             d["Categoria"],
#             d["Preço ingresso"]
#         )

#         workshop.append(w)

#     return workshop


# Lista todos os eventos contidos na lista 'eventos'
def listar_eventos(objeto):
    print("\n" + "="*30)
    print("      LISTA DE EVENTOS")
    print("="*30)

    if not objeto:
        print("Nenhum evento cadastrado ainda.")
        return

    for i, evento in enumerate(objeto):
        print(f"\n--- Evento {i} ---")
        print(evento)

    print("\n" + "="*30)


def add_participante(evento):
    try:
        if not evento:
            print("Nenhum evento disponível.")
            return

        # Chama a função para listar
        listar_eventos(evento)
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
