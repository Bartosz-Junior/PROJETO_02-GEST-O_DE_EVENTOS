import datetime, json

class Evento:
    def __init__(self, nome = None, data_evento = None, local = None, capacidade_max = None, 
                 categoria = None, preco_ingresso = None):
        self._nome = nome
        self._data_evento = data_evento
        self._local  = local
        self._capacidade_max = capacidade_max
        self._categoria = categoria
        self._preco_ingresso = preco_ingresso
        self._data_atual = datetime.datetime.today()

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

    def add_evento(self):                                                    #FUNÇÃO PARA ADD EVENTOS
        try:                                                                 #TRATAMENTO DE ERROS
            print("_" * 35)                                                  #IMPRIMI 35 CARACTERES
            print("Digte [1] para adicionar PALESTRA:")                      #OPÇÕES PARA ADD PALESTRA
            print("Digte [2] para adicionar WORKSHOP:\n")                    #OPÇÃO PARA ADD WORKSHOP
            escolha = int(input())                                           #ESCOLHA DA OPÇÃO 1 OU 2
            if escolha == 1:                                                 #SE ESCOLHA É 1 VAI ADD PALESTRA
                print("__________ Adicionar Palestra __________" )           #IMPRIMI UM CABEÇALHO
                nome = str(input("Tema da palestra: "))                      #RECEBE O NOME DA PALESTRA
                while True:                                                  #LOOP ENQUANTO VERDADEIRO PARA TRATAMENTO DE DATA
                    data_evento = str(input("Data de realização dd/mm/aaaa:"))  #DATA NO FORMATO STRING (ENTRADA)
                    data_formatada = datetime.datetime.strptime(data_evento, "%d/%m/%Y" )   #CONVERTE PARA O FORMATO DATA
                    if data_formatada < self._data_atual:                    #SE DATA INFORMADA FOR MENOR QUE A DATA ATUAL VAI PEDIR A DATA NOVAMENTE
                        print("A data do evento não pode ser menor que a data atual!")  #IMPRIMI MENSAGEM QUE A DATA INFORMADA NÃO É VÁLIDA.
                        continue                                             #CONTINUA O CÓDIGO ATÉ INFORMAR UMA DATA VÁLIDA.
                    else:                                                    #CASO A DATA SEJÁ MAIOR CONTINUA O CÓDIGO PARA O RESTO DO FORMULARIO
                        break                                                #QUEBRA O WHILE PARA CONTINUAR O FORMULARIO
                local_evento = str(input("Local: "))                         #ENTRADA DO LOCAL DO EVENTO (STR)
                capacidade_max = int(input("Capacidade de pessoas: "))       #ENTRADA DA CAPACIDADE MAX. (INT)
                categoria = str(input("Categoria [Tech/Marketing]: "))       #ENTRADA DA CATEGORIA DA PALESTRA
                preco_ingresso = float(input("Preço da entrada: "))          #PREÇO DO INGRESSO
                dados_palestra = {"Tema" : nome, "Data" : data_evento, "Local" : local_evento, "Capacidade" : capacidade_max,
                            "Categoria" : categoria, "Preço ingresso" : preco_ingresso} #DICIONÁRIO QUE É ARMAZENADO NO .JSON
                with open("C:/Users/Júnior/Documents/Projeto_02_BFD/PROJETO_02-GEST-O_DE_EVENTOS/database/palestras.json", "r", encoding= "utf-8") as file:
                    carrega_palestras = json.load(file)
                    carrega_palestras.append(dados_palestra)
                
                with open("C:/Users/Júnior/Documents/Projeto_02_BFD/PROJETO_02-GEST-O_DE_EVENTOS/database/palestras.json", "w", encoding= "utf-8") as file:
                    json.dump(carrega_palestras, file, indent= 4, ensure_ascii= False)

            if escolha == 2:                                                 # SE ESCOLHER 2 ADD WORKSHOP
                print("__________ Adicionar Workshop __________" )           #IMPRIMI UM CABEÇALHO
                nome = str(input("Tema do Workshop: "))                      #RECEBE O NOME DO WORKSHOP
                while True:                                                  #LOOP ENQUENTO VERDADEIRO PARA TRATAMENTO DE DATA
                    data_evento = str(input("Data de realização dd/mm/aaaa: ")) #ENTRADA DE DATA NO FORMATO STRING
                    data_formatada = datetime.datetime.strptime(data_evento, "%d/%m/%Y")    #CONVERTE A DATA PARA DATETIME
                    if data_formatada < self._data_atual:                    #SE A DATA INFORMADA FOR MENOR QUE A DATA ATUAL ELE PEDE A DATA NOVAMENTE
                        print("A data do evento não pode ser menor que a data atual!")  #IMPRIMI UMA MENSAGEM INFORMANDO QUE A DATA INFORMADA É INVÁLIDA
                        continue                                             # CONTINUAR NO LOOP
                    else:                                                    # SE NÃO...
                        break                                                #QUEBRA O LOOP E CONTINUA O FORMULÁRIO
                local_evento = str(input("Local: "))                         # ENTRADA DO LOCAL DO EVENTO(STR)
                capacidade_max = int(input("Capacidade de pessoas: "))       #CAPACIDADE MAX DO EVENTO(INT)
                categoria = str(input("Categoria [Tech/Marketing]: "))       #CATEGORIA DO EVENTO(str)
                preco_ingresso = float(input("Preço da entrada: R$ "))       #PREÇO DA ENTRADA DO EVENTO
                dados_workshop = {"Tema" : nome, "Data" : data_evento, "Local" : local_evento, "Capacidade" : capacidade_max,
                            "Categoria" : categoria, "Preço ingresso" : preco_ingresso}     #DICIONÁRIO COM AS INFORMAÇÕES DO FORMULÁRIO
                
                with open("C:/Users/Júnior/Documents/Projeto_02_BFD/PROJETO_02-GEST-O_DE_EVENTOS/database/wokshop.json", "r", encoding= "utf-8") as file:
                    carrega_workshops = json.load(file)
                    carrega_workshops.append(dados_workshop)

                with open("C:/Users/Júnior/Documents/Projeto_02_BFD/PROJETO_02-GEST-O_DE_EVENTOS/database/wokshop.json", "w", encoding= "utf-8") as file:
                    json.dump(carrega_workshops, file, indent= 4, ensure_ascii= False)
                    
                
        except ValueError:
            print("Opção inválida!")
                
                
    def listar_eventos(self):
        pass        