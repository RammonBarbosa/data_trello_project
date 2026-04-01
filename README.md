📊 Trello Data Pipeline (ETL) com Docker & PostgreSQL

Este projeto demonstra a construção de um pipeline de dados (ETL) profissional, projetado para extrair informações
da API do Trello, realizar transformações e carregar os dados em um banco PostgreSQL para apoio à decisão.

🏗️ Arquitetura do Projeto
O pipeline segue o fluxo: Trello API → Python (Docker) → Transformação → PostgreSQL → Análise (DBeaver/Power BI).

# 1. Extração (extract.py)
O que faz: Consome dados brutos da API do Trello.

Motivo: Isolar a coleta garante que, se a API mudar, apenas este módulo precise de manutenção.

# 2. Transformação (transform.py)
O que faz: Limpeza e modelagem dos dados brutos usando a biblioteca Pandas.

Motivo: Transforma dados complexos da API em tabelas estruturadas prontas para análise.

# 3. Carga (load.py)
O que faz: Utiliza SQLAlchemy para persistir os dados transformados no banco de dados.

Motivo: Garante que os dados sejam inseridos de forma relacional e segura.

# 4. Orquestração (main.py)
 O que faz: O "maestro" que define a ordem de execução de todas as etapas anteriores.

---

🐳 Infraestrutura com Docker
O uso de containers é o diferencial técnico deste projeto por garantir:
Reprodutibilidade: O projeto roda exatamente igual em qualquer máquina.
Isolamento: As dependências (Python, Pandas, bibliotecas SQL) ficam dentro do container, sem sujar seu sistema operacional.
Padronização: Facilita o deploy em ambientes de produção.

---

 📁 Detalhamento dos Arquivos de Configuração
docker-compose.yml: Gerencia os dois serviços (App Python e Banco PostgreSQL). Ele garante que o banco suba antes do código tentar se conectar (depends_on).

Dockerfile: Define a imagem base (Python 3.11-slim) e instala as bibliotecas necessárias listadas no requirements.txt.

data/: Pasta de volume mapeada para garantir que, se o Docker for desligado, as tabelas criadas no Postgres não sejam perdidas.

requirements.txt: Contém as bibliotecas essenciais: requests, pandas, sqlalchemy e psycopg2-binary.

---

 🚀 Como Executar e Validar

1.  Rodar o Projeto:
    docker-compose up --build
   
Este comando sobe automaticamente o container do app e do banco.

2.  Verificar no DBeaver:
    Conecte-se ao banco para validar os dados usando:
    Host: localhost
    User/Password: user / password 
    Database: trello_db

---

💼 Valor de Negócio
Este projeto demonstra domínio em Engenharia de Dados, cobrindo desde a ingestão de APIs até a modelagem em banco relacional e conteinerização.
É a base para criar dashboards de produtividade e análise de performance de equipes.

