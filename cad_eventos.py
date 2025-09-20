import datetime

class CadastroEvento:
    def __init__(self, nome, data_evento, local, capacidade_max, categoria, preco_ingresso):
        self._nome = nome
        self._data_evento = data_evento
        self._local  = local
        self._capacidade_max = capacidade_max
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
    
    def status(self):
        print(f"Nome: {self._nome}\nData: {self._data_evento}\nLocal: {self._local}\nCapacidade: {self._capacidade_max}\nPreço: R$ {self._preco_ingresso}")


mini_curso = CadastroEvento("Mini curso Python", "20/09/2025", "Recife", 50, "Tech", 0)
mini_curso.status()