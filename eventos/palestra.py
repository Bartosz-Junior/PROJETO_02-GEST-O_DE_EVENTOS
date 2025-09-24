from .eventos import Evento

class Palestra(Evento):
    def __init__(self, nome = None, data_evento= None, local = None, capacidade_max = None, categoria = None, preco_ingresso = None):
        super().__init__(nome, data_evento, local, capacidade_max, categoria, preco_ingresso)

    def add_palestra(self):
        nome = str(input("Tema da palestra: "))
        data_evento = str(input("Data de realização: "))
        local_evento = str(input("Local: "))
        capacidade_max = int(input("Capacidade de pessoas: "))
        categoria = str(input("Categoria [Tech/Marketing]: "))
        preco_ingresso = float(input("Preço da entrada: "))
        dados_palestra = {"Palestra: " : nome, "Data: " : data_evento, "Local " : local_evento, "Capacidade: " : capacidade_max,
                 "Categoria: " : categoria, "Preço ingresso: " : preco_ingresso}
        file = open("C:/Users/Júnior/Documents/Projeto_02_BFD/PROJETO_02-GEST-O_DE_EVENTOS/database/palestras.json", "a")
        file.write(str(dados_palestra) + "\n")
        file.close()

    def listar_palestras(self):
        arquivo = open("C:/Users/Júnior/Documents/Projeto_02_BFD/PROJETO_02-GEST-O_DE_EVENTOS/database/palestras.json", "r")
        conteudo = arquivo.readlines()
        for dados in conteudo:
            print(dados)
            print("\n")