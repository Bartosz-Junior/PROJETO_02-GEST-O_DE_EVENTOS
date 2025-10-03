from .eventos import Evento
from utils import helpers_functions, db_functions
import datetime, json


class Workshop(Evento):
    def __init__(self, nome = None, data_evento= None, local = None, capacidade_max = None, num_inscritos = None, categoria = None, preco_ingresso = None):
        super().__init__(nome, data_evento, local, capacidade_max, categoria, preco_ingresso)        
        self._data_atual = datetime.datetime.today()
    
    def add_evento(self):
        print("__________ Adicionar Workshop __________" )           #IMPRIMI UM CABEÇALHO
        nome = str(input("Tema do Workshop: "))                      #RECEBE O NOME DO WORKSHOP
        while True:                                                  #LOOP ENQUENTO VERDADEIRO PARA TRATAMENTO DE DATA
            data_evento = str(input("Data de realização dd/mm/aaaa: ")) #ENTRADA DE DATA NO FORMATO STRING
            data_formatada = datetime.datetime.strptime(data_evento, "%d/%m/%Y")    #CONVERTE A DATA PARA DATETIME
            if data_formatada < self._data_atual:                    #SE A DATA INFORMADA FOR MENOR QUE A DATA ATUAL ELE PEDE A DATA NOVAMENTE
                print("A data do evento não pode ser menor que a data atual!")  #IMPRIMI UMA MENSAGEM INFORMANDO QUE A DATA INFORMADA É INVÁLIDA
                continue                                             # CONTINUAR NO LOOP
            else:                                                    # SE NÃO...
                break                                                #QUEBRA O LOOP E CONTINUA O FORMULÁRIO
        local_evento = str(input("Local: "))                         # ENTRADA DO LOCAL DO EVENTO(STR)
        
        while True:
            capacidade_max = int(input("Capacidade de pessoas: "))   #ENTRADA DA CAPACIDADE MAX. (INT)
            if capacidade_max <= 0:
                print("O evento deve comportar um número maior que zero de pessoas.")
                continue
            else:
                break

        categoria = str(input("Categoria [Tech/Marketing]: ")).lower().strip()       #ENTRADA DA CATEGORIA DA PALESTRA
        while True:
            preco_ingresso = float(input("Preço da entrada: "))      #PREÇO DO INGRESSO
            if preco_ingresso < 0:
                print("O preço não pode ser negativo.")
                continue
            else:
                break       #PREÇO DA ENTRADA DO EVENTO
        dados_workshop = {"Tema" : nome, "Data" : data_evento, "Local" : local_evento, "Capacidade_max" : capacidade_max,
                    "Numero_inscritos" : 0,"Categoria" : categoria, "Preço ingresso": preco_ingresso}     #DICIONÁRIO COM AS INFORMAÇÕES DO FORMULÁRIO
        
        carrega_workshops = db_functions.carregar_json("database/wokshops.json")
        carrega_workshops.append(dados_workshop)

        with open("database\wokshops.json", "w", encoding= "utf-8") as file:
            json.dump(carrega_workshops, file, indent= 4, ensure_ascii= False)
            
    def listar_workshop(self):
        carrega_workshop = db_functions.carregar_json("database\wokshops.json")
        for i,v in enumerate(carrega_workshop):
            print(f"_____ WORKSHOP {i + 1} _____")
            print(f"Tema: {v["Tema"]:5}")
            print(f"Data: {v["Data"]:5}")
            print(f"Local: {v["Local"]:5}")
            print(f"Capacidade: {v["Capacidade_max"]:5}")
            print(f"Categoria: {v["Categoria"]:5}")
            print(f"Preço: R${v["Preço ingresso"]:5.2f}\n")
