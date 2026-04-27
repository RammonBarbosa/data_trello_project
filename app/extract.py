import requests
import os

def extract_data():
    # 1. Carregando variáveis com .strip() para evitar erros de digitação/espaços
    API_KEY = os.getenv('TRELLO_API_KEY', '').strip()
    TOKEN = os.getenv('TRELLO_TOKEN', '').strip()
    BOARD_ID = os.getenv('TRELLO_BOARD_ID', '').strip() 
    
    if not API_KEY or not TOKEN or not BOARD_ID:
        print("ERRO: Variáveis de ambiente (KEY, TOKEN ou BOARD_ID) não encontradas!")
        return []

    params = {'key': API_KEY, 'token': TOKEN, 'limit': 1000}
    all_cards = []
    last_id = None
    
    # URL para buscar as listas (tradução de IDs para nomes)
    url_lists = f"https://api.trello.com/1/boards/{BOARD_ID}/lists"
    # URL para buscar os cartões
    url_cards = f"https://api.trello.com/1/boards/{BOARD_ID}/cards"

    try:
        # 2. Puxando as Listas primeiro
        resp_lists = requests.get(url_lists, params=params)
        mapa_listas = {}
        if resp_lists.status_code == 200:
            listas = resp_lists.json()
            mapa_listas = {lista['id']: lista['name'] for lista in listas}
        else:
            print(f"Aviso: Erro {resp_lists.status_code} ao buscar listas.")

        # 3. Loop de Paginação para buscar todos os cartões (incluindo o 1680º!)
        while True:
            if last_id:
                params['before'] = last_id
            
            response = requests.get(url_cards, params=params)
            
            if response.status_code != 200:
                print(f"Erro na extração de cartões: {response.status_code}")
                print(f"Resposta da API: {response.text}")
                break
                
            batch = response.json()
            if not batch:
                break
                
            all_cards.extend(batch)
            last_id = batch[-1]['id'] # Marca o último cartão para o próximo lote
            
            print(f"Progresso: {len(all_cards)} cartões capturados...")

            if len(batch) < 1000: # Se veio menos de 1000, acabou o quadro
                break

        # 4. Injetando o nome da lista em cada cartão
        for cartao in all_cards:
            cartao['nome_lista'] = mapa_listas.get(cartao['idList'], 'Desconhecida')

        print(f"Extração concluída com sucesso: {len(all_cards)} cartões processados!")
        return all_cards

    except Exception as e:
        print(f"Erro inesperado na extração: {e}")
        return []