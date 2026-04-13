📊 Trello Data Pipeline (ETL) & API Gateway

Docker | Python | FastAPI | Supabase (PostgreSQL) | GitHub Actions | BI Integration

Este projeto apresenta um pipeline de dados ETL robusto integrado a uma API Gateway de alta disponibilidade. A solução extrai dados operacionais da API do Trello, processa-os via Python e os disponibiliza através de uma interface REST padronizada, facilitando o consumo por diversas ferramentas de Business Intelligence e análise de dados.

🏗️ Arquitetura e Fluxo de Dados:
O sistema foi projetado para garantir integridade e agilidade no acesso à informação:

Ingestão de Dados (main.py): Sincronização automatizada entre a API do Trello e o PostgreSQL (Supabase).

Camada de Abstração (FastAPI - api.py): Uma API que atua como middleware, desacoplando o banco de dados do consumidor final. Isso permite que qualquer ferramenta que suporte requisições HTTP consuma os dados de forma estruturada.

Consumo Multiplataforma (BI Tools): A entrega via JSON facilita a integração com Power BI, Tableau, Looker, Metabase ou scripts de Data Science (Jupyter/Pandas).

☁️ Diferenciais Técnicos (V3.0):
Nesta versão, o projeto consolidou-se como uma infraestrutura de dados moderna:

FastAPI Gateway: Exposição de endpoints performáticos para servir os 1662+ registros de forma assíncrona.

Orquestração On-Startup: Configuração de gatilhos automáticos que garantem a atualização do banco de dados no momento em que a infraestrutura é iniciada.

Escalabilidade via Docker: Ambiente totalmente conteinerizado, permitindo o deploy rápido em provedores de nuvem (PaaS) ou servidores on-premise.

Resiliência de Dados: Uso de SQLAlchemy e processos de Upsert para evitar duplicidade e garantir a fidelidade do histórico.

📂 Estrutura do Projeto:
app/api.py: Backend em FastAPI responsável pela distribuição dos dados.

app/main.py: Núcleo do pipeline ETL (Extract, Transform, Load).

Dockerfile: Definição da imagem para ambiente de produção.

docker-compose.yml: Orquestração de serviços, volumes e rede.

🚀 Execução e Acesso:
Configure as variáveis de ambiente no arquivo .env (credenciais Supabase e Trello).

Inicie a infraestrutura:

Bash
docker-compose up -d --build
Consuma os dados via: http://localhost:8000/cartoes

📊 Integração com Ferramentas de BI:
A grande vantagem desta arquitetura é a versatilidade. Como os dados são entregues via REST API, a conexão não depende de drivers específicos de banco de dados ou portas restritas:

No Power BI/Tableau: Utilize o conector Web/API nativo.

No Python/R: Utilize bibliotecas de requisição HTTP para análises estatísticas.

Vantagem: Redução de latência e maior segurança, pois o banco de dados não fica exposto diretamente à rede externa.

💼 Valor de Negócio:
Esta solução transforma o Trello de uma ferramenta de gestão de tarefas em uma fonte de dados estratégica. O projeto demonstra competência em Engenharia de Dados e Desenvolvimento Backend, focando em fornecer dados limpos, atualizados e de fácil acesso para tomadores de decisão, independentemente da ferramenta de visualização escolhida.