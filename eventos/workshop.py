from .eventos import Evento
import datetime

class Workshop(Evento):
    def __init__(self, tema, data, local, capacidade_max, numero_inscritos, categoria, preco_ingresso):

        super().__init__(tema, data, local, capacidade_max, numero_inscritos, categoria, preco_ingresso)

    def __str__(self):
        return (
            f"Tema: {self.tema}\n"
            f"Data: {self.data}\n"
            f"Local: {self.local}\n"
            f"Capacidade_max: {self.capacidade_max}\n"
            f"Inscritos: {self.numero_inscritos}\n"
            f"Categoria: {self.categoria}\n"
            f"Preço: R$ {self.preco:.2f}\n"
        )