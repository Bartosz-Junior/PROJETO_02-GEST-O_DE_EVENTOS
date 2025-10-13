from utils import db_functions
from datetime import datetime

class Evento:
    def __init__(self, tema, data, local, capacidade_max, numero_inscritos, categoria, tipo, preco_ingresso):
        
        self._tema = tema
        self._data = datetime.strptime(data, "%d/%m/%Y")
        self._local  = local
        self._capacidade_max = capacidade_max
        self._numero_inscritos = numero_inscritos
        self._categoria = categoria
        self._tipo = tipo
        self._preco_ingresso = preco_ingresso

    @property
    def tema(self):
        return self._tema
    
    @property
    def data(self):
        return self._data
    
    @property
    def local(self):
        return self._local
    
    @property
    def capacidade_max(self):
        return self._capacidade_max
    
    @property
    def numero_inscritos(self):
        return self._numero_inscritos
    
    @property
    def categoria(self):
        return self._categoria
    
    @property
    def tipo(self):
        return self.tipo
    
    @property
    def preco(self):
        return self._preco_ingresso
    
    def salvar_evento_json(self):
        
        data_str = self.data.strftime("%d/%m/%Y")

        dict_evento = {
            "tema" : self.tema,
            "data" : data_str,
            "local" : self.local,
            "capacidade_max" : self.capacidade_max, 
            "numero_inscritos" : self.numero_inscritos,
            "categoria" : self.categoria,
            "tipo" : self.tipo,
            "preco_ingresso" : self.preco
        }

        dados = db_functions.carregar_json("database/palestras.json")
        dados.append(dict_evento)
        db_functions.salvar_json("database/palestras.json", dados)

    #VERIFICAR SE A DATA É FUTURA
    def verificar_data(self):
        pass
    
    def reduzir_numero_inscritos(self):
        raise NotImplementedError("Este método deve ser subescrito pelas subclasses.")  
        
    def verificar_vagas(self):
        pass

    def aumentar_numero_inscritos(self):
        raise NotImplementedError("Este método deve ser subescrito pelas subclasses.")
        

    # SUBSTITUI O METODO DETALHES() SOLICITADO NA DOCUMENTAÇÃO
    def __str__(self):

        raise NotImplementedError("Este método deve ser subescrito pelas subclasses.")  