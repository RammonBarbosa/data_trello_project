from extract import extract_data
from transform import transform_data
from load import save_to_postgres

def run_pipeline():
    print("--- Iniciando Pipeline ETL Trello ---")
    
    # 1. Busca os dados (Extract)
    dados_brutos = extract_data()
    
    # 2. Limpa e organiza (Transform)
    dados_limpos = transform_data(dados_brutos)
    
    # 3. Salva no Postgres (Load) - Sua etapa 7!
    if not dados_limpos.empty:
        save_to_postgres(dados_limpos)
    else:
        print("Nenhum dado para salvar.")

if __name__ == "__main__":
    run_pipeline()