import datetime

class Evento:
    def __init__(self, nome = None, data_evento = None, local = None, capacidade_max = None, 
                 categoria = None, preco_ingresso = None):
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

    def add_evento(self):
        pass

    def listar_eventos(self):
        for evento in self.eventos:
            print(evento)

#mini_curso = CadastroEvento("Mini curso Python", 20/9/2025,"Recife",0,"Tech", 0)
#mini_curso.status()

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
        arquivo = open("C:/Users/Júnior/Documents/Projeto_02_BFD/PROJETO_02-GEST-O_DE_EVENTOS/workshop.txt", "r")
        conteudo = arquivo.readlines()
        for dados in conteudo:
            print(dados)
            print("\n")

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
        file = open("palestras.txt", "a")
        file.write(str(dados_palestra) + "\n")
        file.close()

    def listar_palestras(self):
        arquivo = open("C:/Users/Júnior/Documents/Projeto_02_BFD/PROJETO_02-GEST-O_DE_EVENTOS/palestras.txt", "r")
        conteudo = arquivo.readlines()
        for dados in conteudo:
            print(dados)
            print("\n")
    