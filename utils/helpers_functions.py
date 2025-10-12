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

            novo_evento.salvar_evento_json()


        elif tipo_evento == "workshop":
            novo_evento = Workshop(tema, data, local_evento, capacidade_max, numero_inscritos, categoria, preco_ingresso)

            novo_evento.salvar_evento_json()


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


def add_participante(eventos, tipo, diretorio_evento):
    try:
        if not eventos:
            print("Nenhum evento disponível.")
            return

        listar_objetos(eventos, tipo)
        indice = int(input("Informe qual evento deseja participar: "))

        if (indice < 0) or (indice >= len(eventos)):
            print("Evento inválido!")
            return
        
        nome = str(input("Informe o nome do participante: ")).upper()
        email = str(input("Informe o e-mail do particante: ")).lower()
        evento_escolhido = eventos[indice]
        
        if nome and email and evento_escolhido:
            participante = Participante(nome, email, evento_escolhido.tema)
            print(participante)

            if participante.verificar_email("database/participantes.json"):
                return

            participante.salvar_participante_json("database/participantes.json")

            evento_escolhido.aumentar_numero_inscritos(diretorio_evento)

            print("Participante cadastrado com sucesso!")

        else:
            print("Informe todos os dados.")

    except ValueError:
        print("Dados informados inválidos")

    except IndexError:
        print("Evento inválido! O número do evento não existe na lista.")


def buscar_eventos(eventos_filtrados):
    while True:
        
        print("______ BUSCAR EVENTO ______")
        print()
        filtro_tipo = str(input("Informe o tipo do evento [ENTER para ignorar filtro]: ")).lower()
        filtro_data = str(input("Informe a data do evento (dd/mm/YY) [ENTER para ignorar filtro]: "))
        filtro_categoria = str(input("Informe a categoria do evento [ENTER para ignorar filtro]: ")).lower()

        if filtro_tipo:
            if filtro_tipo == "palestras":
                eventos_filtrados = [evento for evento in eventos_filtrados if isinstance(evento, Palestra)]

            elif filtro_tipo == "workshops":
                eventos_filtrados = [evento for evento in eventos_filtrados if isinstance(evento, Workshop)]

        if filtro_categoria:
            eventos_filtrados = [evento for evento in eventos_filtrados if evento.categoria == filtro_categoria]

        if filtro_data:
            try:
                filtro_data_formatada = datetime.datetime.strptime(filtro_data, "%d/%m/%Y")
                eventos_filtrados = [evento for evento in eventos_filtrados if evento.data.date() == filtro_data_formatada.date()]
                
            except ValueError:
                print("Data inválida. Use o formato dd/mm/aaaa.")

        if eventos_filtrados:
            print(f"Total de {len(eventos_filtrados)} encontrados!")
            listar_objetos(eventos_filtrados, "RESULTADOS")

        else:
            print("Total de 0 eventos encontrados!")