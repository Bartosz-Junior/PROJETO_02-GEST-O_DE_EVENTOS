# FUNÇOES RELACIONADAS AOS BANCO DE DADOS

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


# REINSTÂNCIA TODOS OS OBJETOS CARREGADOS DO JSON
def carregar_instancias(dados, instancia_evento):

    eventos = []
    for dado in dados:
        
        p = instancia_evento(
            dado["Tema"],
            dado["Data"],
            dado["Local"],
            dado["Capacidade_max"],
            dado["Numero_inscritos"],
            dado["Categoria"],
            dado["Preço ingresso"]
        )
        eventos.append(p)

    return eventos