from .eventos import Evento

class Palestra(Evento):
    def __init__(self, nome = None, data_evento= None, local = None, capacidade_max = None, categoria = None, preco_ingresso = None):
        super().__init__(nome, data_evento, local, capacidade_max, categoria, preco_ingresso)
    
    def add_evento(self):
        return super().add_evento()

    def listar_palestras(self):
        arquivo = open("C:/Users/Júnior/Documents/Projeto_02_BFD/PROJETO_02-GEST-O_DE_EVENTOS/database/palestras.json", "r")
        conteudo = arquivo.readlines()
        for dados in conteudo:
            print(dados)
            print("\n")
        arquivo.close()