import pandas as pd

def transform_data(raw_json):
    if not raw_json:
        return pd.DataFrame()

    df = pd.DataFrame(raw_json)
    
    # Tratamento das Etiquetas (continua perfeito!)
    df['etiquetas'] = df['labels'].apply(
        lambda x: ', '.join([l['name'] for l in x]) if isinstance(x, list) else ''
    )
    
    # O 'nome_lista' já vem pronto da extração, é só selecionar!
    cols_interessantes = ['name', 'desc', 'dateLastActivity', 'idList', 'nome_lista', 'etiquetas']
    df_clean = df[cols_interessantes].copy()
    
    # Renomear para português
    df_clean.columns = ['nome_tarefa', 'descricao', 'ultima_atividade', 'id_lista', 'nome_lista', 'etiquetas']
    
    print(f"Transformação concluída: {len(df_clean)} tarefas processadas com sucesso.")
    return df_clean