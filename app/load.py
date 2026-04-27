import os
import pandas as pd
from sqlalchemy import create_engine

def save_to_postgres(df):
    # O GitHub Actions injeta o DIRECT_URL aqui automaticamente
    database_url = os.getenv("DIRECT_URL")
    
    if not database_url:
        print("❌ Erro: DIRECT_URL não encontrada. Verifique os Secrets do GitHub.")
        return

    print("Conectando ao Supabase para salvar os dados...")
    
    try:
        # Criando a conexão
        # pool_pre_ping ajuda a manter a conexão viva em ambientes de nuvem
        engine = create_engine(database_url, pool_pre_ping=True)
        
        # O 'replace' é vital para limpar os duplicados e manter os 1681 cartões
        df.to_sql("cards", engine, if_exists="replace", index=False)
        
        print(f"✅ SUCESSO! {len(df)} cartões salvos no Supabase.")
        
    except Exception as e:
        print(f"❌ Erro na carga para o banco: {e}")

# Se você quiser testar este arquivo isoladamente (opcional)
if __name__ == "__main__":
    # Apenas para teste local, cria um DF vazio
    test_df = pd.DataFrame()
    save_to_postgres(test_df)