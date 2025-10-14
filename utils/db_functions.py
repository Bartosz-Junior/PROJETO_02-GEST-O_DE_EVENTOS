# FUNÇOES RELACIONADAS AOS BANCO DE DADOS
from datetime import datetime
import json
import os # para verificar se o arquivo json existe


# TENTA CARREGAR QUALQUER LISTA DE UM ARQUIVO JSON E RETORNA UM DICT
def carregar_json(diretorio):

    if not os.path.exists(diretorio):
        return []

    try:
        with open(diretorio, "r", encoding="utf-8") as file:
            dados = json.load(file)
            return dados

    except json.JSONDecodeError:
        print(f"Erro ao decodificar JSON do arquivo '{diretorio}'")
        return []
    
    except Exception as e:
        print(f"Erro inesperado: {e}")
        return []

def salvar_json(diretorio, dados):

    with open(diretorio, "w", encoding="utf-8") as file:
        json.dump(dados, file, indent=4, ensure_ascii=False)


def carregar_objeto(dado, classe):

    objeto = classe(**dado)
    return objeto

def carregar_dict_dados():
    DIRETORIO_PALESTRAS = "database/palestras.json"
    DIRETORIO_WORKSHOPS = "database/workshops.json"
    DIRETORIO_PARTICIPANTES = "database/participantes.json"

    dicts_palestras = carregar_json(DIRETORIO_PALESTRAS)
    dicts_workshops = carregar_json(DIRETORIO_WORKSHOPS)
    dicts_participantes = carregar_json(DIRETORIO_PARTICIPANTES)

    hoje = datetime.now()

    dict_dados = {
        "palestras" : [],
        "workshops" : [],
        "participantes" : []
    }

    for evento in dicts_palestras:
        data_str = evento["data"]
        data = datetime.strptime(data_str, "%d/%m/%Y")

        if data > hoje:
            dict_dados["palestras"].append(evento)
            
    for evento in dicts_workshops:
        data_str = evento["data"]
        data = datetime.strptime(data_str, "%d/%m/%Y")

        if data > hoje:
            dict_dados["workshops"].append(evento)

    dict_dados["participantes"] = dicts_participantes

    return dict_dados