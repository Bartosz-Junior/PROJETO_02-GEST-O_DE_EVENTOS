# FUNÇOES RELACIONADAS AOS BANCO DE DADOS
from eventos.palestra import Palestra
from eventos.workshop import Workshop
from eventos.participantes import Participante
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

# REINSTÂNCIA TODOS OS OBJETOS CARREGADOS DO JSON
def carregar_instancias(dados, classe):

    lista_instancias = []
    for dado in dados:
        
        p = classe(**dado)
        lista_instancias.append(p)

    return lista_instancias

def carregar_todos_dados():
    DIRETORIO_PALESTRAS = "database/palestras.json"
    DIRETORIO_WORKSHOPS = "database/workshops.json"
    DIRETORIO_PARTICIPANTES = "database/participantes.json"

    # CARREGA OS DADOS DO JSON E A VARIAVEL RECEBER UM DICT
    dict_palestras = carregar_json(DIRETORIO_PALESTRAS)
    dict_workshops = carregar_json(DIRETORIO_WORKSHOPS)
    dict_participantes = carregar_json(DIRETORIO_PARTICIPANTES)

    return dict_palestras, dict_workshops, dict_participantes