from .eventos import Evento
import json, datetime

class Palestra(Evento):
    def __init__(self, nome = None, data_evento= None, local = None, capacidade_max = None, num_inscritos = None, categoria = None, preco_ingresso = None):
        super().__init__(nome, data_evento, local, capacidade_max, num_inscritos, categoria, preco_ingresso)
        self._data_atual = datetime.datetime.today()

    
    def add_evento(self):
        print("__________ Adicionar Palestra __________" )              #IMPRIMI UM CABEÇALHO
        nome = str(input("Tema da palestra: "))                         #RECEBE O NOME DA PALESTRA
        while True:                                                     #LOOP ENQUANTO VERDADEIRO PARA TRATAMENTO DE DATA
            data_evento = str(input("Data de realização dd/mm/aaaa: "))  #DATA NO FORMATO STRING (ENTRADA)
            data_formatada = datetime.datetime.strptime(data_evento, "%d/%m/%Y" )   #CONVERTE PARA O FORMATO DATA
            if data_formatada < self._data_atual:                       #SE DATA INFORMADA FOR MENOR QUE A DATA ATUAL VAI PEDIR A DATA NOVAMENTE
                print("A data do evento não pode ser menor que a data atual!")  #IMPRIMI MENSAGEM QUE A DATA INFORMADA NÃO É VÁLIDA.
                continue                                                #CONTINUA O CÓDIGO ATÉ INFORMAR UMA DATA VÁLIDA.
            else:                                                       #CASO A DATA SEJÁ MAIOR CONTINUA O CÓDIGO PARA O RESTO DO FORMULARIO
                break                                                   #QUEBRA O WHILE PARA CONTINUAR O FORMULARIO
        local_evento = str(input("Local: "))                            #ENTRADA DO LOCAL DO EVENTO (STR)
        
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
                break

        dados_palestra = {"Tema" : nome, "Data" : data_evento, "Local" : local_evento, "Capacidade_max" : capacidade_max,
                    "Categoria" : categoria, "Preço ingresso" : preco_ingresso} #DICIONÁRIO QUE É ARMAZENADO NO .JSON
        
        with open("database/palestras.json", "r", encoding= "utf-8") as file:
            carrega_palestras = json.load(file)
            carrega_palestras.append(dados_palestra)
        
        with open("database/palestras.json", "w", encoding= "utf-8") as file:
            json.dump(carrega_palestras, file, indent= 4, ensure_ascii= False)

    def listar_palestras(self):
        with open("database/palestras.json", "r", encoding= "utf-8") as file:
            carrega_palestras = json.load(file)
            for i,v in enumerate(carrega_palestras):
                print(f"_____ PALESTRA {i + 1} _____")
                print(f"Tema: {v["Tema"]:5}")
                print(f"Data: {v["Data"]:5}")
                print(f"Local: {v["Local"]:5}")
                print(f"Capacidade: {v["Capacidade_max"]:5}")
                print(f"Categoria: {v["Categoria"]:5}")
                print(f"Preço: R${v["Preço ingresso"]:5.2f}\n")
