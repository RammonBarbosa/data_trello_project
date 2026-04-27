import os
from sqlalchemy import create_engine

def save_to_postgres(df):
    # 1. Puxa a URL e já remove espaços em branco que podem vir do GitHub
    database_url = os.getenv("DIRECT_URL", "").strip()
    
    if not database_url:
        print("❌ Erro: DIRECT_URL não encontrada.")
        return

    # 2. Garante o prefixo correto para o SQLAlchemy moderno
    # Se começar com postgres:// ou postgresql://, transformamos no formato completo
    if database_url.startswith("postgres://"):
        database_url = database_url.replace("postgres://", "postgresql+psycopg2://", 1)
    elif database_url.startswith("postgresql://"):
        database_url = database_url.replace("postgresql://", "postgresql+psycopg2://", 1)

    print("Conectando ao Supabase...")
    
    try:
        # 3. Cria o engine com a URL tratada
        engine = create_engine(database_url, pool_pre_ping=True)
        
        # O 'replace' vai limpar a bagunça anterior e deixar o número exato
        df.to_sql("cards", engine, if_exists="replace", index=False)
        
        print(f"✅ SUCESSO! {len(df)} cartões salvos no Supabase.")
        
    except Exception as e:
        print(f"❌ Erro na carga para o banco: {e}")