from fastapi import FastAPI
from sqlalchemy import create_engine
import pandas as pd
import os
import subprocess 

app = FastAPI()

# 1. Configurações de conexão
DATABASE_URL = os.getenv("DIRECT_URL")

# 2. O Evento de Startup (Coloque aqui)
@app.on_event("startup")
def atualizar_dados_na_inicializacao():
    print("--- Iniciando atualização automática (Trello -> Supabase) ---")
    try:
        # Executa o seu script de carga
        subprocess.run(["python", "main.py"], check=True)
        print("--- Atualização concluída com sucesso! ---")
    except Exception as e:
        print(f"--- Erro ao rodar o main.py: {e} ---")

# 3. Seus Endpoints (As rotas da API)
@app.get("/")
def home():
    return {"status": "API Online", "mensagem": "Dados sendo sincronizados no startup"}

@app.get("/cartoes")
def get_cartoes():
    engine = create_engine(DATABASE_URL)
    try:
        df = pd.read_sql("SELECT * FROM cards", engine)
        return df.to_dict(orient="records")
    except Exception as e:
        return {"error": f"Erro ao acessar o banco: {str(e)}"}