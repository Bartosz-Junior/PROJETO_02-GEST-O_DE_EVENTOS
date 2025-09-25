from .eventos import Evento

class Palestra(Evento):
    def __init__(self, nome = None, data_evento= None, local = None, capacidade_max = None, categoria = None, preco_ingresso = None):
        super().__init__(nome, data_evento, local, capacidade_max, categoria, preco_ingresso)
    
    def add_evento(self):
        return super().add_evento()

    def listar_palestras(self):
        pass