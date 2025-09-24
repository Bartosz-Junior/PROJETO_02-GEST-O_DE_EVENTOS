from .eventos import Evento


class Workshop(Evento):
    def __init__(self, nome = None, data_evento= None, local = None, capacidade_max = None, categoria = None, preco_ingresso = None):
        super().__init__(nome, data_evento, local, capacidade_max, categoria, preco_ingresso)

    def add_workshop(self):
        nome = str(input("Tema do Workshop: "))
        data_evento = str(input("Data de realização: "))
        local_evento = str(input("Local: "))
        capacidade_max = int(input("Capacidade de pessoas: "))
        categoria = str(input("Categoria [Tech/Marketing]: "))
        preco_ingresso = float(input("Preço da entrada: R$ "))
        dados_workshop = {"Palestra: " : nome, "Data: " : data_evento, "Local " : local_evento, "Capacidade: " : capacidade_max,
                 "Categoria: " : categoria, "Preço ingresso: " : preco_ingresso}
        file = open("workshop.txt", "a")
        file.write(str(dados_workshop) + "\n")
        file.close()

    def listar_workshop(self):
        arquivo = open("C:/Users/Júnior/Documents/Projeto_02_BFD/PROJETO_02-GEST-O_DE_EVENTOS/database/wokshop.json", "r")
        conteudo = arquivo.readlines()
        for dados in conteudo:
            print(dados)
            print("\n")