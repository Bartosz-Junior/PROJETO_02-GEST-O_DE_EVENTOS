# FUNÇÕES RELACIONADAS A MAIN/MENU PRINCIPAL

from utils import helpers_functions

def adicionar_evento():
    while True:
        try:
            print("__________ ADICIONAR EVENTO __________")
            print()
            print("Digite [1] para PALESTRAS:")
            print("Digite [2] para WORKSHOPS:")
            print("Digite [0] para VOLTAR:")
            escolha = int(input())

            if escolha == 1:
                helpers_functions.add_evento("palestra")

            elif escolha == 2:
                helpers_functions.add_evento("workshop")

            elif escolha == 0:
                break

        except ValueError:
            print("Opção inválida!")


def mostrar_eventos(dict_dados):
    while True:
        try:
            print("________ EVENTOS DISPONIVEIS ________")
            print()
            print("Digite [1] TODOS:")
            print("Digite [2] BUSCAR POR:")
            print("Digite [0] VOLTAR:")
            escolha = int(input())

            if escolha == 1:
                helpers_functions.listar_dados(dict_dados["palestras"], "palestras")
                helpers_functions.listar_dados(dict_dados["workshops"], "workshops")

            elif escolha == 2:
                helpers_functions.buscar_eventos(dict_dados)

            elif escolha == 0:
                break

        except ValueError:
            print("Opção inválida!")


def fazer_inscricao(dict_dados):
    print("________ INSCREVER PARTICIPANTE ________")
    print()
    print("Digite [1] para PALESTRAS:")
    print("Digite [2] para WORKSHOPS:")

    try:
        escolha_evento = int(input("Escolha o tipo de evento: "))

        if escolha_evento == 1:
            helpers_functions.add_participante(
                dict_dados["palestras"], "palestras", "database/palestras.json"
            )

        elif escolha_evento == 2:
            helpers_functions.add_participante(
                dict_dados["workshops"], "workshops", "database/workshops.json"
            )

        else:
            print("Opção inválida! Digite 1 para Palestras ou 2 para Workshops.")

    except ValueError:
        print("Entrada inválida! Digite apenas números inteiros (1 ou 2).")

    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")


def buscar_email_cancelamento(dict_dados):
    email = str(input("Escolha o e-mail para realizar o cancelamento da inscrição: "))

    for participante in dict_dados["participantes"]:
        if email == participante["email"]:
            helpers_functions.cancelar_inscricao_participante(participante, dict_dados)
            break
    else:
        print("E-mail não encontrado.") 

def buscar_email_checkin(dict_dados):

    email = str(input("Escolha o e-mail para realizar o check-in: "))

    for participante in dict_dados["participantes"]:

        if email == participante["email"]:
            helpers_functions.fazer_checkin_participante(participante)
            break
    else:
        print("E-mail não encontrado.")

def relatorios(dict_dados):
    print("\n===== RELATÓRIOS =====\n")

    # validação básica do parâmetro
    if not isinstance(dict_dados, dict):
        print("Erro: o parâmetro deve ser um dicionário com chaves 'palestras', 'workshops' e 'participantes'.")
        return

    palestras = dict_dados.get("palestras", [])
    workshops = dict_dados.get("workshops", [])
    participantes = dict_dados.get("participantes", [])

    # Totais de eventos
    total_palestras = len(palestras)
    total_workshops = len(workshops)
    total_eventos = total_palestras + total_workshops
    print(f"Total de palestras: {total_palestras}")
    print(f"Total de workshops: {total_workshops}")
    print(f"Total de eventos: {total_eventos}\n")

    # Número total de inscritos por evento
    print("Inscrições por evento:")
    total_inscritos_via_evento = 0
    for tipo, lista in (("palestra", palestras), ("workshop", workshops)):
        if not lista:
            continue
        print(f"\n>>> {tipo.upper()}S")
        for evento in lista:
            tema = evento.get("tema")
            inscritos = evento.get("numero_inscritos", 0)
  
            print(f"- {tema}: {inscritos} inscritos")
            total_inscritos_via_evento += inscritos

    print(f"\n >>> Total geral de participantes: {total_inscritos_via_evento}")

    # Lista de eventos com vagas disponíveis
    print("\n >>> Eventos com vagas disponíveis:")
    encontrados_vagas = False
    for tipo, lista in (("palestra", palestras), ("workshop", workshops)):
        for evento in lista:
            tema = evento.get("tema", "<sem tema>")
            capacidade = evento.get("capacidade_max")
            inscritos = evento.get("numero_inscritos", 0)

            if capacidade is None:
                # não dá para calcular vagas se capacidade inválida
                continue
            vagas = capacidade - inscritos

            if vagas > 0:
                encontrados_vagas = True
                print(f"- {tema} ({tipo}) — {vagas} vagas disponíveis ({inscritos}/{capacidade})")

    if not encontrados_vagas:
        print("Nenhum evento com vagas disponíveis no momento.")

    # Calcular a receita total de um evento específico
    print("\nCalcular receita total de um evento específico")
    nome_evento = input("Digite o nome do evento (ou ENTER para pular): ").strip()
    if nome_evento:
        achou = False
        for lista in (palestras, workshops):
            for evento in lista:
                if evento.get("tema", "").lower() == nome_evento.lower():
                    achou = True
                    try:
                        inscritos = int(evento.get("numero_inscritos", 0))
                    except (ValueError, TypeError):
                        inscritos = 0
                    try:
                        preco = float(evento.get("preco_ingresso", evento.get("preco", 0)))
                    except (ValueError, TypeError):
                        preco = 0.0
                    receita = inscritos * preco
                    print(f"\n >>> Receita do evento '{evento.get('tema')}': {inscritos} x R$ {preco:.2f} = R$ {receita:.2f}\n")
                    break
            if achou:
                break
        if not achou:
            print(f"Evento '{nome_evento}' não encontrado.")
    else:
        print("Cálculo de receita pulado pelo usuário.")

    print("\n===== FIM DOS RELATÓRIOS =====\n")

