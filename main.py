from utils import menu_functions, helpers_functions, db_functions
from eventos.palestra import Palestra
from eventos.workshop import Workshop

DIRETORIO_PALESTRAS = 'database/palestras.json'
DIRETORIO_WORKSHOPS = 'database/wokshops.json'
DIRETORIO_PARTICIPANTES = "database/participantes.json"

# CARREGA OS DADOS DO JSON E A VARIAVEL RECEBER UM DICT
palestras = db_functions.carregar_json(DIRETORIO_PALESTRAS)
workshops = db_functions.carregar_json(DIRETORIO_WORKSHOPS)
participantes = db_functions.carregar_json(DIRETORIO_PARTICIPANTES)


objetos_palestras = db_functions.carregar_instancias(palestras, Palestra)
objetos_workshops = db_functions.carregar_instancias(workshops, Workshop)


while True:
    try:
        print("______________ MENU _______________")
        print("_" * 35)
        print("[1] Adicionar evento")
        print("[2] Mostrar eventos")
        print("[3] Fazer inscrição")
        print("[4] Cancelar inscrição")
        print("[5] pass")
        print("[0] Sair")
        print('_' * 35)
        escolha = int(input("Escolha uma opção: "))

        match escolha:
            case 1:
                menu_functions.adicionar_evento()
                
            case 2:
                menu_functions.mostrar_eventos()

            case 3:
                menu_functions.fazer_inscricao(objetos_palestras, objetos_workshops)        

            case 4:
                menu_functions.cancelar_inscricao()

            case 5:
                pass

            case 0:
                print("Saindo...")
                break

            case _:
                print("Digite uma opção válida!")

    except ValueError:
        print("Erro! Digite um número inteiro, ou 0 para sair.\n")
        continue