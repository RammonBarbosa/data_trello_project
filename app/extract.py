import requests
import os

def extract_data():
    API_KEY = os.getenv('TRELLO_API_KEY')
    TOKEN = os.getenv('TRELLO_TOKEN')
    BOARD_ID = os.getenv('TRELLO_BOARD_ID') 
    
    params = {'key': API_KEY, 'token': TOKEN}

    # 1. Puxando os Cartões
    url_cards = f"https://api.trello.com/1/boards/{BOARD_ID}/cards"
    resp_cards = requests.get(url_cards, params=params)
    
    # 2. Puxando as Listas 
    url_lists = f"https://api.trello.com/1/boards/{BOARD_ID}/lists"
    resp_lists = requests.get(url_lists, params=params)
    
    if resp_cards.status_code == 200 and resp_lists.status_code == 200:
        cartoes = resp_cards.json()
        listas = resp_lists.json()
        
        # Criando o Dicionário de Tradução 
        mapa_listas = {lista['id']: lista['name'] for lista in listas}
        
        # Injetando o nome correto em cada cartão
        for cartao in cartoes:
            # Pega o ID da lista do cartão, procura no mapa, e salva o nome
            cartao['nome_lista'] = mapa_listas.get(cartao['idList'], 'Desconhecida')
            
        print("Extração concluída com sucesso (Cartões e Listas combinados)!")
        return cartoes
    else:
        print("Erro na extração!")
        return []
