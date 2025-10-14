# FUNÇÕES AUXILIARES

from utils import db_functions
from eventos.palestra import Palestra
from eventos.workshop import Workshop
from eventos.participantes import Participante
from datetime import datetime


def add_evento(tipo_evento):
    hoje = datetime.today()
    
    print(f"__________ Adicionar {tipo_evento.capitalize()} __________")

    # 1. Validação de Tema
    while True:
        tema = str(input("Tema: ")).strip()
        if not tema:
            print("O tema não pode ser vazio!")
            continue
        break

    # 2. Validação de Data (já está boa, apenas movendo o try/except para dentro)
    while True:
        try:
            data = input("Data de realização (dd/mm/aaaa): ")
            # tenta converter
            data_formatada = datetime.strptime(data, "%d/%m/%Y")      
            # valida se é no passado
            if data_formatada < hoje:
                print("A data do evento não pode ser menor que a data atual!")
                continue 
            # se tudo certo, sai do loop
            break

        except ValueError:
            print("Formato inválido! Digite a data no formato dd/mm/aaaa.\n")
            continue

    # 3. Validação de Local
    while True:
        local_evento = str(input("Local: ")).strip()
        if not local_evento:
            print("O local não pode ser vazio!")
            continue
        break
    
    # 4. Validação de Capacidade Máxima (incluindo try/except para int)
    while True:
        try:
            capacidade_max_str = input("Capacidade de pessoas: ")
            capacidade_max = int(capacidade_max_str)
            if capacidade_max <= 0:
                print("O evento deve comportar um número maior que zero de pessoas.")
                continue
            else:
                break
        except ValueError:
            print("Capacidade inválida! Digite um número inteiro maior que zero.\n")
            continue


    while True:
        categoria = str(input("Categoria [Tech/Marketing]: ")).lower().strip()
        if not categoria:
             print("A categoria não pode ser vazia!")
             continue

        break
        
    numero_inscritos = 0

    # 6. Validação de Preço (incluindo try/except para float)
    while True:
        try:
            preco_ingresso_str = input("Preço da entrada: ")
            preco_ingresso = float(preco_ingresso_str)
            if preco_ingresso < 0:
                print("O preço não pode ser negativo.")
                continue
            else:
                break
        except ValueError:
            print("Preço inválido! Digite um número (ex: 50.00).\n")
            continue

    try:
        if tipo_evento == "palestra":
            tipo = tipo_evento
            
            novo_evento = Palestra(tema, data, local_evento, capacidade_max, numero_inscritos, categoria, tipo, preco_ingresso)
            novo_evento.salvar_evento_json()
            print(f"Evento 'Palestra' criado (Tema: {tema}, Data: {data}, Preço: {preco_ingresso})")


        elif tipo_evento == "workshop":
            tipo = tipo_evento
            
            novo_evento = Workshop(tema, data, local_evento, capacidade_max, numero_inscritos, categoria, tipo, preco_ingresso)
            novo_evento.salvar_evento_json()
            print(f"Evento 'Workshop' criado (Tema: {tema}, Data: {data}, Preço: {preco_ingresso})")
        
        else:
            # Caso o 'tipo_evento' passado para a função seja inválido
            print(f"Erro: Tipo de evento '{tipo_evento}' não suportado.")
            return

        print("Evento cadastrado com sucesso!")

    except Exception as e:
        # Tratamento genérico para erros durante a instanciação ou salvamento
        print(f"Ocorreu um erro inesperado ao salvar o evento: {e}")


def listar_dados(dados, tipo):
    print("\n" + "="*30)
    print(f"      LISTA DE {tipo.upper()}")
    print("="*30)

    if not dados:
        print(f"Nenhum {tipo.lower()} cadastrado ainda.")
        return

    for i, dado in enumerate(dados):
        print(f"\n--- {tipo} {i} ---")

        for chave, valor in dado.items():
            print(f"{chave.capitalize()}: {valor}")

    print("\n" + "="*30)

def add_participante(eventos, tipo, diretorio_evento):
    try:
        if not eventos:
            print("Nenhum evento disponível.")
            return

        listar_dados(eventos, tipo)
        indice = int(input("Informe qual evento deseja participar: "))

        if (indice < 0) or (indice >= len(eventos)):
            print("Evento inválido!")
            return
        
        nome = str(input("Informe o nome do participante: ")).upper()
        email = str(input("Informe o e-mail do particante: ")).lower()
        evento_escolhido = db_functions.carregar_objeto(eventos[indice], Palestra)
        
        if nome and email and evento_escolhido:
            participante = Participante(nome, email, evento_escolhido.tema)

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

def cancelar_inscricao_participante(participante):
    objeto_participante = db_functions.carregar_objeto(participante, Participante)

    evento = objeto_participante.remover_inscrito()
    buscar_evento_inscrito(evento)

def buscar_evento_inscrito(evento):

    # VERFICAR O TIPO DO EVENTO
    dados_palestras = db_functions.carregar_json(f"database/palestras.json")
    dados_workshops = db_functions.carregar_json(f"database/workshops.json")
    
    # Descobrir onde o evento está
    for dado in dados_palestras:
        if dado["tema"] == evento:
            dados = dados_palestras
            break
    else:
        dados = dados_workshops

    for dado in dados:
        if dado["tema"] == evento:
            if dado["tipo"] == "palestra":
                objeto_evento = db_functions.carregar_objeto(dado, Palestra)
            else:
                objeto_evento = db_functions.carregar_objeto(dado, Workshop)

            objeto_evento.reduzir_numero_inscritos()
            break
    else:
        print("Evento não encontrado")


def buscar_eventos(dict_dados):
    while True:
        try:

            print("______ BUSCAR EVENTO ______")
            print()

            while True:
                filtro_tipo = str(input("Informe o tipo do evento [ENTER para ignorar filtro]: ")).lower()
                if filtro_tipo in dict_dados:
                    break
                print("Tipo invalido, escolha entre palestras ou workshops.\n")


            filtro_data = str(input("Informe a data do evento (dd/mm/YY) [ENTER para ignorar filtro]: "))
            filtro_categoria = str(input("Informe a categoria do evento [ENTER para ignorar filtro]: ")).lower()

        except ValueError:
            print("Opção inválida!")
            continue

        if filtro_tipo:
            if filtro_tipo == "palestras":
                eventos_filtrados = dict_dados["palestras"]

            elif filtro_tipo == "workshops":
                eventos_filtrados = dict_dados["workshops"]

        if filtro_categoria:
            eventos_filtrados = [evento for evento in eventos_filtrados if evento["categoria"] == filtro_categoria]

        if filtro_data:
            try:
                eventos_filtrados = [evento for evento in eventos_filtrados if evento["data"] == filtro_data]
                
            except ValueError:
                print("Data inválida. Use o formato dd/mm/aaaa.")

        if eventos_filtrados:
            print()
            print(f"Total de {len(eventos_filtrados)} encontrados!")
            listar_dados(eventos_filtrados, "resultados")
            break

        else:
            print()
            print("Total de 0 eventos encontrados!\n")
            break
        
def fazer_checkin_participante(participante):
    objeto_participante = db_functions.carregar_objeto(participante, Participante)

    objeto_participante.fazer_checkin()