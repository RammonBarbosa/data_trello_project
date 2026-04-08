import os
from sqlalchemy import create_engine
from dotenv import load_dotenv

load_dotenv()

def save_to_postgres(df):
    # Puxando o nome exato que você colocou no .env
    database_url = os.getenv("DIRECT_URL")
    
    if not database_url:
        print("❌ Erro: DIRECT_URL não encontrada no arquivo .env")
        return

    # Criando o engine com 'pool_pre_ping' (verifica se a conexão está viva)
    # e 'isolation_level' para resolver o erro de transação inválida
    engine = create_engine(
        database_url,
        pool_pre_ping=True,
        isolation_level="AUTOCOMMIT"
    )

    print("Conectando via DIRECT_URL ao Supabase...")
    
    try:
        # Enviando os dados
        df.to_sql("cards", engine, if_exists="replace", index=False)
        print("✅ SUCESSO! Dados salvos no Supabase via Direct URL.")
    except Exception as e:
        print(f"❌ Erro na carga: {e}")