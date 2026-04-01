from sqlalchemy import create_engine

def save_to_postgres(df):
    
#Função para conectar ao banco e salvar os dados do Trello.
#Criamos a conexão (A Ponte)
#Importante: usamos 'db' porque é o nome do serviço no docker-compose
    engine = create_engine("postgresql://user:password@db:5432/trello_db")
#Enviamos os dados (O Transporte)
    print("Enviando dados para o PostgreSQL...")
    df.to_sql("cards", engine, if_exists="replace", index=False)
    
    print("Dados salvos com sucesso na tabela 'cards'!")