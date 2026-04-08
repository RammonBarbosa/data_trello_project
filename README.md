📊 Trello Data Pipeline (ETL) Cloud Native
Docker | Python | Supabase (PostgreSQL) | GitHub Actions | Power BI

Este projeto apresenta um pipeline de dados ETL (Extract, Transform, Load) completo e automatizado. Ele extrai dados da API do Trello, processa-os via Python e os armazena em um banco de dados PostgreSQL na nuvem (Supabase), com atualização automática via GitHub Actions.

🏗️ Arquitetura e Fluxo de Dados
O pipeline foi desenhado seguindo as melhores práticas de engenharia de dados, garantindo desacoplamento e escalabilidade:

Extração (extract.py): Consome dados brutos (JSON) da API do Trello.

Transformação (transform.py): Realiza a limpeza, tratamento de tipos e modelagem relacional utilizando Pandas.

Carga (load.py): Utiliza SQLAlchemy para persistir os dados no Supabase, utilizando uma DIRECT_URL para garantir estabilidade em cargas volumosas.

Orquestração (main.py): Gerencia a execução sequencial das etapas.

☁️ Diferenciais Técnicos (V2.0)
Nesta versão, o projeto evoluiu de uma infraestrutura local para uma solução Cloud-First:

Banco de Dados em Nuvem: Substituição do Postgres local pelo Supabase, permitindo acesso global aos dados e integração direta com ferramentas de BI sem necessidade de tunelamento.

Automação com CI/CD (GitHub Actions): O pipeline é executado automaticamente todos os dias às 08:00 (Horário de Brasília), garantindo que o dashboard esteja sempre atualizado sem intervenção humana.

Segurança (Secrets): Uso de variáveis de ambiente e GitHub Secrets para proteger credenciais sensíveis (API Keys e Connection Strings).

Dockerização Profissional: O ambiente é totalmente isolado via Docker, garantindo que o script rode de forma idêntica tanto no computador local quanto nos servidores do GitHub.

📁 Estrutura do Projeto
.github/workflows/automation.yml: Configuração da automação agendada no GitHub.

Dockerfile & docker-compose.yml: Definições da infraestrutura como código.

.env: (Não versionado) Armazena chaves de API e URLs de conexão local.

requirements.txt: Dependências do projeto (requests, pandas, sqlalchemy, psycopg2-binary, python-dotenv).

🚀 Como Executar Localmente
Clone o repositório.

Configure seu arquivo .env com as chaves do Trello e a URI do Supabase.

Execute o comando:

Bash
docker-compose up --build
Os logs do terminal confirmarão a carga bem-sucedida na nuvem.

📊 Visualização de Dados
Os dados armazenados no Supabase estão conectados diretamente ao Power BI, permitindo análises de:

Volume de tarefas por lista (Backlog, Em Análise, Concluído).

Lead Time e performance de entrega.

Monitoramento de gargalos em tempo real.

💼 Valor de Negócio
Este projeto demonstra domínio em Engenharia de Dados Moderna, cobrindo ingestão de APIs, tratamento de dados complexos, conteinerização e automação em nuvem. É uma solução real para empresas que buscam transformar dados operacionais do Trello em inteligência estratégica.