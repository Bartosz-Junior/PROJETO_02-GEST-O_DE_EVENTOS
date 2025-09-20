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

    @nome.setter
    def nome(self):
        nome_evento = str(input("Nome do evento: "))
        if nome_evento != "":
            self._nome = nome_evento
        else:
            print("O nome do evento não pode ser vazio.")
    
    @data.setter
    def data(self, data_evento):
        data_evento = str(input("Data do evento (DD/MM/AA): "))
        data_str = datetime.date.strptime(data_evento, '%d/%m/%a')
        if data_str > datetime.date.today():
            self._data_evento = data_str
        else:
            print("A data do evento não pode ser anterior a data atual.")

    @local.setter
    def local(self):
        local_evento = str(input("Local do evento: "))
        self._local = local_evento
        
    @capacidade_max.setter
    def capacidade_max(self):
        capacidade = int(input("Informe o número de pessoas suportado: "))
        if capacidade > 0:
            self._capacidade_max = capacidade
        else:
            print("O evento não pode ter capacidade menor de que zero(0)!")

    @categoria.setter
    def categoria(self):
        categoria_evento = str(input("Categoria do evento (Tech, Marketing): "))
        self.categoria = categoria_evento

    @preco.setter
    def preco(self, preco_ingresso):
        self._preco_ingresso = preco_ingresso
    
    def status(self):
        print(f"Nome: {self.nome}\nData: {self.data}\nLocal: {self.local}\nCapacidade: {self.capacidade_max}\nPreço: R$ {self.preco}")


#mini_curso = CadastroEvento("Mini curso Python", 20/9/2025,"Recife",0,"Tech", 0)
#mini_curso.status()
