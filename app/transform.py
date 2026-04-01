import pandas as pd

def transform_data(raw_json):
    if not raw_json:
        return pd.DataFrame()

    # Transforma o JSON bruto em uma tabela (DataFrame)
    df = pd.DataFrame(raw_json)
    
    # Seleciona apenas as colunas que interessam para análise
    # Exemplo: Nome do cartão, Descrição, Data de última atividade
    cols_interessantes = ['name', 'desc', 'dateLastActivity', 'idList']
    df_clean = df[cols_interessantes].copy()
    
    # Renomeia para português para ficar mais fácil no DBeaver
    df_clean.columns = ['nome_tarefa', 'descricao', 'ultima_atividade', 'id_lista']
    
    print(f"Transformação concluída: {len(df_clean)} tarefas processadas.")
    return df_clean