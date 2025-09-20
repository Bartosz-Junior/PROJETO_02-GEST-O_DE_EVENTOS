import cad_eventos
eventos_cadastrados = []

meu_evento = cad_eventos.CadastroEvento(str(input("Nome do evento: ")), str(input("Data do evento: ")), 
                                        str(input("Local do eventO: ")), int(input("Capacidade máxima: ")), str(input("Categoria do evento: ")),
                                        float(input("Preço do ingresso: ")))

eventos_cadastrados.append({meu_evento})
meu_evento.status()
print(eventos_cadastrados)
