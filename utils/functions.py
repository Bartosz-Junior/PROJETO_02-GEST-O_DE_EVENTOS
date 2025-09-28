import json, datetime

# funções auxiliares

def function():
    pass

def buscar_evento_data():
    with open("database/palestras.json", "r", encoding="utf-8") as file:
        carrega_palestras = json.load(file)

    with open("database/wokshop.json", "r", encoding="utf-8") as file:
        carrega_workshops = json.load(file)

        data_busca = str(input("Informe a data do evento (dd/mm/aaaa): "))

        print("__________ PALESTRAS __________")
        for i, v in enumerate(carrega_palestras):
            if v["Data"] == data_busca:
                print(f"{i + 1:}- Tema: {v["Tema"]:5} Data: {v["Data"]:5} Local: {v["Local"]:5} Capacidade: {v["Capacidade"]:5} Categoria: {v["Categoria"]:5} Preço: R${v["Preço ingresso"]:5.2f}\n")


        print("__________ WORKSHOPS __________")
        for i, v in enumerate(carrega_workshops):
            if v["Data"] == data_busca:
                print(f"{i + 1:}- Tema: {v["Tema"]:5} Data: {v["Data"]:5} Local: {v["Local"]:5} Capacidade: {v["Capacidade"]:5} Categoria: {v["Categoria"]:5} Preço: R${v["Preço ingresso"]:5.2f}\n")