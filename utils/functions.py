import json, datetime

# funções auxiliares

def buscar_evento_data():
    with open("database/palestras.json", "r", encoding="utf-8") as file:
        carrega_palestras = json.load(file)

    with open("database/wokshop.json", "r", encoding="utf-8") as file:
        carrega_workshops = json.load(file)

        data_busca = str(input("Informe a data do evento (dd/mm/aaaa): "))

        print("__________ PALESTRAS __________")
        for i, v in enumerate(carrega_palestras):
            if v["Data"] == data_busca:
                print(f"{i + 1:}- Tema: {v["Tema"]:5} Data: {v["Data"]:5} Local: {v["Local"]:5} Capacidade: {v["Capacidade"]:5} Categoria: {v["Categoria"]:5} Preço: R${v["Preço ingresso"]:5.2f}\n")


        print("__________ WORKSHOPS __________")
        for i, v in enumerate(carrega_workshops):
            if v["Data"] == data_busca:
                print(f"{i + 1:}- Tema: {v["Tema"]:5} Data: {v["Data"]:5} Local: {v["Local"]:5} Capacidade: {v["Capacidade"]:5} Categoria: {v["Categoria"]:5} Preço: R${v["Preço ingresso"]:5.2f}\n")

def buscar_evento_categoria():
    with open("database/palestras.json", "r", encoding="utf-8") as file:
        carrega_palestras = json.load(file)

    with open("database/wokshop.json", "r", encoding="utf-8") as file:
        carrega_workshops = json.load(file)

        categoria_busca = str(input("Informe a categoria do evento:")).lower().strip()

        print("__________ PALESTRAS __________")
        for i, v in enumerate(carrega_palestras):
            if v["Categoria"] == categoria_busca:
                print(f"{i + 1:}- Tema: {v["Tema"]:5} Data: {v["Data"]:5} Local: {v["Local"]:5} Capacidade: {v["Capacidade"]:5} Categoria: {v["Categoria"]:5} Preço: R${v["Preço ingresso"]:5.2f}\n")

        print("__________ WORKSHOPS __________")
        for i, v in enumerate(carrega_workshops):
            if v["Categoria"] == categoria_busca:
                print(f"{i + 1:}- Tema: {v["Tema"]:5} Data: {v["Data"]:5} Local: {v["Local"]:5} Capacidade: {v["Capacidade"]:5} Categoria: {v["Categoria"]:5} Preço: R${v["Preço ingresso"]:5.2f}\n")

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
        with open(arquivo, "r", encoding="utf-8"):
            dados = json.load(arquivo)
            return dados

    except json.JSONDecodeError:
        print(f"Erro ao decodificar JSON do arquivo '{arquivo}'")
        return []
    
    except Exception as e:
        print(f"Erro inesperado: {e}")
        return []


def carregar_instancias(dados):

    palestras = []
    for d in dados:
        # recria objeto Palestra
        p = Palestra(
            d["Tema"],
            d["Data"],
            d["Local"],
            d["Capacidade_max"],
            d["Numero_inscritos"],
            d["Categoria"],
            d["Preço ingresso"]
        )

        palestras.append(p)

    return palestras

def carregar_instancias(dados):

    workshop = []

    for d in dados:
        # recria objeto Palestra
        w = Workshop(
            d["Tema"],
            d["Data"],
            d["Local"],
            d["Capacidade_max"],
            d["Numero_inscritos"],
            d["Categoria"],
            d["Preço ingresso"]
        )

        workshop.append(w)

    return workshop


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


def add_participante(palestras, workshop):
    try:
        if (not palestras) and (not workshop):
            print("Nenhum evento disponível.")
            return

        print("*** ADICIONAR PARTICIPANTE ***")
        tipo_evento = int(input("Escolha o tipo de evento: [1] Palestra | [2] Workshop"))

        if tipo_evento == 1:

            # Chama a função para listar
            listar_eventos(palestras)
            indice = int(input("Informe qual evento deseja participar: "))

            if (indice < 0) or (indice >= len(palestras)):
                print("Evento inválido!")
                return
            
            nome = str(input("Informe o nome: ")).upper()
            email = str(input("Informe o e-mail: ")).lower()
            evento_escolhido = palestras[indice]
            
            if nome and email and evento_escolhido:
                participante = Participante(nome, email, evento_escolhido.nome)
                print(participante)

                dados_participante = {
                    "Nome:": participante.nome,
                    "E-mail": participante.email,
                    "Evento escolhido": participante.evento
                }

                with open("database/participantes.json", "r", encoding= "utf-8") as file:
                        carrega_participantes = json.load(file)
                        carrega_participantes.append(dados_participante)
                    
                with open("database/participantes.json", "w", encoding= "utf-8") as file:
                        json.dump(carrega_participantes, file, indent= 4, ensure_ascii= False)

                evento_escolhido.adicionar_inscrito()

        elif tipo_evento == 2:
            
            # Chama a função para listar
            listar_eventos(workshop)
            indice = int(input("Informe qual evento deseja participar: "))
            
            if (indice < 0) or (indice >= len(workshop)):
                print("Evento inválido!")
                return
            
            nome = str(input("Informe o nome: ")).upper()
            email = str(input("Informe o e-mail: ")).lower()
            evento_escolhido = workshop[indice]
            
            if nome and email and evento_escolhido:
                participante = Participante(nome, email, evento_escolhido.nome)

                dados_participante = {
                    "Nome:": participante.nome,
                    "E-mail": participante.email,
                    "Evento escolhido": participante.evento
                }

                with open("database/participantes.json", "r", encoding= "utf-8") as file:
                        carrega_participantes = json.load(file)
                        carrega_participantes.append(dados_participante)
                    
                with open("database/participantes.json", "w", encoding= "utf-8") as file:
                        json.dump(carrega_participantes, file, indent= 4, ensure_ascii= False)

                evento_escolhido.adicionar_inscrito()

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
