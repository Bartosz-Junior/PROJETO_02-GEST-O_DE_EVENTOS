#  Sistema de Gerenciamento de Eventos  

Este projeto é um sistema back-end para gerenciamento de eventos como workshops, palestras e meetups. Ele permite o **cadastro de eventos**, **inscrição de participantes**, **check-in**, e a **emissão de relatórios detalhados**, funcionando como a espinha dorsal de uma plataforma de gestão.  

##  Funcionalidades  
- **Cadastro de Eventos**: nome, data, local, capacidade máxima, categoria e preço do ingresso.  
- **Inscrição de Participantes**: controle de vagas e verificação de e-mail duplicado.  
- **Gerenciamento do Sistema**:  
  - Listar eventos.  
  - Buscar por categoria ou data.  
  - Cancelar inscrição de participante.  
  - Check-in de participantes.  
- **Relatórios e Análises**:  
  - Número total de inscritos por evento.  
  - Lista de eventos com vagas disponíveis.  
  - Receita total de um evento específico.  

##  Tecnologias Utilizadas  
- **Python 3.x**  
- **Programação Orientada a Objetos (POO)**  
- **JSON** (para persistência dos dados)  
- **Testes Automatizados** (com unittest)  
- **Git e GitHub** (para versionamento)  

##  Estrutura do Projeto  

A estrutura atual do projeto é:  

PROJETO_02-GEST-O_DE_EVENTOS/
│
├── database/
│ ├── palestras.json
│ ├── participantes.json
│ └── wokshop.json
│
├── eventos/
│ ├── eventos.py
│ ├── palestra.py
│ ├── participantes.py
│ ├── sistema.py
│ └── workshop.py
│
├── tests/
│ ├── test_evento.py
│ ├── test_participante.py
│ └── test_system.py
│
├── utils/
│ └── functions.py
│
├── .gitignore
├── inscricao_participante.py
├── main.py
└── README.md