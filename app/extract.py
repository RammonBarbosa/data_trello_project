import requests
import os
def extract_data():
    API_KEY = os.getenv('TRELLO_API_KEY')
    TOKEN = os.getenv('TRELLO_TOKEN')
    BOARD_ID = 'GstiuzaC' # Aquele código que aparece na URL do seu quadro
    
    url = f"https://api.trello.com/1/boards/{BOARD_ID}/cards?key={API_KEY}&token={TOKEN}"
    response = requests.get(url)
    if response.status_code == 200:
        print("Extração concluída com sucesso!")
        return response.json() # Retorna uma lista de dicionários (JSON)
    else:
        print(f"Erro na extração: {response.status_code}")
        return []