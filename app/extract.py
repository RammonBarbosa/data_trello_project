import requests
import os

def extract_data():
    API_KEY = os.getenv('TRELLO_API_KEY')
    TOKEN = os.getenv('TRELLO_TOKEN')
    BOARD_ID = os.getenv('TRELLO_BOARD_ID') 
    
    # Adicionamos 'limit': 1000 para garantir que pegamos o máximo por lote
    params = {'key': API_KEY, 'token': TOKEN, 'limit': 1000}

    # 1. Puxando as Listas 
    url_lists = f"https://api.trello.com/1/boards/{BOARD_ID}/lists"
    resp_lists = requests.get(url_lists, params=params)
    listas = resp_lists.json() if resp_lists.status_code == 200 else []
    mapa_listas = {lista['id']: lista['name'] for lista in listas}

    # 2. Puxando os Cartões com Paginação
    all_cards = []
    last_id = None
    url_cards = f"https://api.trello.com/1/boards/{BOARD_ID}/cards"

    while True:
        # Se já temos o ID do último cartão do lote anterior, usamos o 'before'
        if last_id:
            params['before'] = last_id
        
        response = requests.get(url_cards, params=params)
        
        if response.status_code != 200:
            print(f"Erro na extração: {response.status_code}")
            break
            
        batch = response.json()
        
        if not batch: # Se a lista vier vazia, terminamos
            break
            
        all_cards.extend(batch)
        last_id = batch[-1]['id'] # Guardamos o ID do último para a próxima volta
        
        print(f"Lote capturado: {len(all_cards)} cartões processados...")

        # Se o lote veio com menos de 1000, significa que não há mais cartões
        if len(batch) < 1000:
            break

    # 3. Injetando o nome da lista
    for cartao in all_cards:
        cartao['nome_lista'] = mapa_listas.get(cartao['idList'], 'Desconhecida')

    print(f"Extração total concluída: {len(all_cards)} cartões!")
    return all_cards