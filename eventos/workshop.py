from .eventos import Evento
from utils import db_functions

class Workshop(Evento):
    def __init__(self, tema, data, local, capacidade_max, numero_inscritos, categoria, preco_ingresso):

        super().__init__(tema, data, local, capacidade_max, numero_inscritos, categoria, preco_ingresso)

    def aumentar_numero_inscritos(self):
        super().aumentar_numero_inscritos()
        if self.numero_inscritos > self.capacidade_max:

            dados = db_functions.carregar_json("database/workshops.json")
            for dado in dados:
                if dado["tema"] == self.tema:
                    dado["numero_inscritos"] += 1

            db_functions.salvar_json("database/worshops.json", dados)
        else:
            print("Evento com a capacidade máxima atingida!")

    def reduzir_numero_inscritos(self):
        super().reduzir_numero_inscritos()
        if self.numero_inscritos > 0:
            dados = db_functions.carregar_json("database/workshops.json")
            for dado in dados:
                if dado["tema"] == self.tema:
                    dado["numero_inscritos"] -= 1
            db_functions.salvar_json("database/workshops.json")
        else:
            print("O número de inscritos já está em 0.")

    def __str__(self):
        
        data_str = self.data.strftime("%d/%m/%Y")
        return (
            f"Tema: {self.tema}\n"
            f"Data: {data_str}\n"
            f"Local: {self.local}\n"
            f"Capacidade_max: {self.capacidade_max}\n"
            f"Inscritos: {self.numero_inscritos}\n"
            f"Categoria: {self.categoria}\n"
            f"Preço: R$ {self.preco:.2f}\n"
        )