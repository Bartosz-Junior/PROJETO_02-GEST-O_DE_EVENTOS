# FUNÇÕES AUXILIARES

from eventos.palestra import Palestra
from eventos.workshop import Workshop
from eventos.participantes import Participante

# from eventos.participante import Participante
from datetime import datetime
import json
import os # para verificar se o arquivo json existe
EVENTOS = 'database/palestras.json'



# Tenta carregar a lista de eventos do arquivo JSON.
def carregar_eventos():
    
    if not os.path.exists(EVENTOS):
        # Se o arquivo não existir, retorna uma lista vazia
        return []
    
    try:
        with open(EVENTOS, 'r', encoding='utf-8') as arquivo:
            # Carrega a lista de dicionários do arquivo
            eventos_carregados = json.load(arquivo)
            # Garante que o que foi carregado é uma lista
            if isinstance(eventos_carregados, list):
                return eventos_carregados
            else:
                print(f"Aviso: O arquivo '{EVENTOS}' não contém uma lista válida.")
                return []
            
    except json.JSONDecodeError:
        print(f"Erro ao decodificar JSON do arquivo '{EVENTOS}'. O arquivo pode estar corrompido.")
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

    # Itera sobre a lista de eventos para imprimir cada um
    for i, evento in enumerate(eventos, 1):
        print(f"\n--- Evento {i} ---")
        # Itera sobre as chaves e valores do dicionário (evento)
        for chave, valor in evento.items():
            print(f"  {chave}: {valor}")
    
    print("\n" + "="*30)


def adicionar_evento():
    print("Tipo de evento: [1] Palestra | [2] Workshop")


def add_participante(eventos):
    try:
        if not eventos:
            print("Nenhum evento disponível.")
            return

        # Chama a função para listar
        listar_eventos(eventos)

        print("*** ADICIONAR PARTICIPANTE ***")
        nome = str(input("Informe o nome: "))
        email = str(input("Informe o e-mail: "))
        escolha_evento = int(input("Informe qual evento deseja participar: "))

        participante = Participante(nome, email, escolha_evento)

    except ValueError:
        print("Dados informados inválidos")
