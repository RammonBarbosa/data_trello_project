import requests
import os

def extract_data():
    API_KEY = os.getenv('TRELLO_API_KEY')
    TOKEN = os.getenv('TRELLO_TOKEN')
    BOARD_ID = os.getenv('TRELLO_BOARD_ID') 
    
    # DEBUGAR:
    print(f"DEBUG: KEY={API_KEY[:5] if API_KEY else 'NULA'}, BOARD={BOARD_ID}")
    
    if not API_KEY or not TOKEN or not BOARD_ID:
        print("ERRO: Uma ou mais variáveis de ambiente não foram carregadas!")
        return []

    # Parâmetros base
    params = {'key': API_KEY, 'token': TOKEN, 'limit': 1000}

    # 1. Puxando as Listas 
    url_lists = f"https://api.trello.com/1/boards/{BOARD_ID}/lists"
    resp_lists = requests.get(url_lists, params=params)
    listas = resp_lists.json() if resp_lists.status_code == 200 else []
    mapa_listas = {lista['id']: lista['name'] for lista in listas}

    # 2. Puxando os Cartões com Paginação e Filtro de Duplicatas
    all_cards = []
    seen_ids = set() 
    last_id = None
    url_cards = f"https://api.trello.com/1/boards/{BOARD_ID}/cards"

    while True:
        if last_id:
            params['before'] = last_id
        
        response = requests.get(url_cards, params=params)
        
        if response.status_code != 200:
            print(f"Erro na extração: {response.status_code}")
            break
            
        batch = response.json()
        
        if not batch:
            break
            
        # Filtra apenas o que ainda não vimos nesta rodada
        new_cards = [c for c in batch if c['id'] not in seen_ids]
        
        if not new_cards:
            break
            
        all_cards.extend(new_cards)
        
        # Alimenta o set de IDs para a próxima verificação
        for c in new_cards:
            seen_ids.add(c['id'])
            
        last_id = batch[-1]['id']
        print(f"Lote capturado: {len(all_cards)} cartões únicos...")

        if len(batch) < 1000:
            break

    # 3. Injetando o nome da lista
    for cartao in all_cards:
        cartao['nome_lista'] = mapa_listas.get(cartao['idList'], 'Desconhecida')

    print(f"Extração total concluída: {len(all_cards)} cartões!")
    return all_cards