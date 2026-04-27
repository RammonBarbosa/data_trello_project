import os
import re
from sqlalchemy import create_engine

def save_to_postgres(df):
    # 1. Puxa a URL e remove QUALQUER espaço, aspas ou quebra de linha
    raw_url = os.getenv("DIRECT_URL", "")
    # Limpeza profunda usando Regex para garantir que só sobrou a string da URL
    database_url = re.sub(r'[\"\'\s\t\n\r]', '', raw_url)
    
    if not database_url:
        print("❌ Erro: DIRECT_URL está vazia nos Secrets do GitHub!")
        return

    # 2. Forçar o protocolo correto (postgresql+psycopg2)
    # O Supabase costuma dar a URL começando com postgres://, o que o SQLAlchemy novo não aceita
    if database_url.startswith("postgres://"):
        database_url = database_url.replace("postgres://", "postgresql+psycopg2://", 1)
    elif database_url.startswith("postgresql://"):
        database_url = database_url.replace("postgresql://", "postgresql+psycopg2://", 1)

    print("Conectando ao Supabase...")
    
    try:
        # 3. Criar engine com timeout para não ficar travado
        engine = create_engine(
            database_url, 
            pool_pre_ping=True,
            connect_args={"connect_timeout": 10}
        )
        
        # O 'replace' vai finalmente limpar as 6723 linhas e deixar as 1684 reais
        df.to_sql("cards", engine, if_exists="replace", index=False)
        
        print(f"✅ SUCESSO! {len(df)} cartões salvos no Supabase.")
        
    except Exception as e:
        # Se falhar aqui, o print abaixo vai nos mostrar como a URL começa (sem a senha)
        prefixo = database_url.split('@')[0] if '@' in database_url else "URL_MALFORMADA"
        print(f"❌ Erro na carga: {e}")
        print(f"DEBUG: Prefixo da URL utilizada: {prefixo.split(':')[0]}")