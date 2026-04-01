import requests

def extract_data():
    # Substitua pelas suas chaves do Trello (conseguidas no Trello Power-Up Admin)
    API_KEY = 'SUA_KEY_AQUI'
    TOKEN = 'SEU_TOKEN_AQUI'
    BOARD_ID = 'ID_DO_SEU_QUADRO' # Aquele código que aparece na URL do seu quadro
    
    url = f"https://api.trello.com/1/boards/{BOARD_ID}/cards?key={API_KEY}&token={TOKEN}"
    
    response = requests.get(url)
    if response.status_code == 200:
        print("Extração concluída com sucesso!")
        return response.json() # Retorna uma lista de dicionários (JSON)
    else:
        print(f"Erro na extração: {response.status_code}")
        return []