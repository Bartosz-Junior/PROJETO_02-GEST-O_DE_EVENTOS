# FUNÇÕES AUXILIARES

from eventos.palestra import Palestra
from eventos.workshop import Workshop
from eventos.participantes import Participante

# from eventos.participante import Participante
from datetime import datetime
import json
import os # para verificar se o arquivo json existe
PALESTRAS = 'database/palestras.json'
WORKSHOP = 'database/workshop.json'



# TENTA CARREGAR A LISTA DE PALESTRAS DO ARQUIVO JSON
def carregar_palestras():

    if not os.path.exists(PALESTRAS):
        return []

    try:
        with open(PALESTRAS, "r", encoding="utf-8") as arquivo:
            dados = json.load(arquivo)
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

    except json.JSONDecodeError:
        print(f"Erro ao decodificar JSON do arquivo '{PALESTRAS}'")
        return []
    except Exception as e:
        print(f"Erro inesperado: {e}")
        return []
    
# TENTA CARREGAR A LISTA DE WORKSHOP DO ARQUIVO JSON
def carregar_workshop():
    
    if not os.path.exists(WORKSHOP):
        # Se o arquivo não existir, retorna uma lista vazia
        return []
    
    try:
        with open(WORKSHOP, 'r', encoding='utf-8') as arquivo:
            # Carrega a lista de dicionários do arquivo
            eventos_carregados = json.load(arquivo)
            # Garante que o que foi carregado é uma lista
            if isinstance(eventos_carregados, list):
                return eventos_carregados
            else:
                print(f"Aviso: O arquivo '{WORKSHOP}' não contém uma lista válida.")
                return []
            
    except json.JSONDecodeError:
        print(f"Erro ao decodificar JSON do arquivo '{WORKSHOP}'. O arquivo pode estar corrompido.")
        return []
    except Exception as e:
        print(f"Erro inesperado ao ler o arquivo: {e}")
        return []


# Lista todos os eventos contidos na lista 'eventos'
def listar_eventos(eventos):
    print("\n" + "="*30)
    print("      LISTA DE EVENTOS")
    print("="*30)

    if not eventos:
        print("Nenhum evento cadastrado ainda.")
        return

    for i, evento in enumerate(eventos, 1):
        print(f"\n--- Evento {i} ---")
        print(evento)

    print("\n" + "="*30)


def adicionar_evento():
    print("Tipo de evento: [1] Palestra | [2] Workshop")


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
            indice = int(input("Informe qual evento deseja participar: ")) - 1
            if (indice < 0) or (indice > len(palestras)):
                print("Evento inválido!")
                return
            
            
            nome = str(input("Informe o nome: "))
            email = str(input("Informe o e-mail: "))
            evento_escolhido = palestras[indice]
            
            participante = Participante(nome, email, evento_escolhido.nome)
            evento_escolhido.adicionar_inscrito()

        elif tipo_evento == 2:
            
            # Chama a função para listar
            listar_eventos(workshop)
            indice = int(input("Informe qual evento deseja participar: "))
            if indice < 0 or indice > len(workshop):
                print("Evento inválido!")
                return
            
            
            nome = str(input("Informe o nome: "))
            email = str(input("Informe o e-mail: "))
            evento_escolhido = workshop[indice].nome
            
            participante = Participante(nome, email, evento_escolhido)
            workshop[indice].capacidade -= 1

    except ValueError:
        print("Dados informados inválidos")
