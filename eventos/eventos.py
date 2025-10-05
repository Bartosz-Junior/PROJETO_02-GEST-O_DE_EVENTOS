import datetime, json

class Evento:
    def __init__(self, nome, data_evento, local, capacidade_max, numero_inscritos, categoria, preco_ingresso):
        self._nome = nome
        self._data_evento = data_evento
        self._local  = local
        self._capacidade_max = capacidade_max
        self.numero_inscritos = numero_inscritos
        self._categoria = categoria
        self._preco_ingresso = preco_ingresso

    @property
    def nome(self):
        return self._nome
    
    @property
    def data(self):
        return self._data_evento
    
    @property
    def local(self):
        return self._local
    
    @property
    def capacidade_max(self):
        return self._capacidade_max
    
    @property
    def categoria(self):
        return self._categoria
    
    @property
    def preco(self):
        return self._preco_ingresso
    

    def __str__(self):
        return (
            f"Tema: {self.nome}\n"
            f"Data: {self.data}\n"
            f"Local: {self.local}\n"
            f"Capacidade_max: {self.capacidade_max}\n"
            f"Inscritos: {self.numero_inscritos}\n"
            f"Categoria: {self.categoria}\n"
            f"Preço: R$ {self.preco:.2f}\n"
        )     