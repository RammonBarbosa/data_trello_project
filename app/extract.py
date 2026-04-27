import requests
import os

def extract_data():
    # 1. Carregamento seguro das variáveis de ambiente
    API_KEY = os.getenv('TRELLO_API_KEY', '').strip()
    TOKEN = os.getenv('TRELLO_TOKEN', '').strip()
    BOARD_ID = os.getenv('TRELLO_BOARD_ID', '').strip() 
    
    if not API_KEY or not TOKEN or not BOARD_ID:
        print("❌ ERRO: Variáveis de ambiente (KEY, TOKEN ou BOARD_ID) não encontradas!")
        return []

    # 2. Configuração dos parâmetros com filtro 'visible'
    # O 'filter': 'visible' garante que cartões arquivados não entrem na conta
    params = {
        'key': API_KEY, 
        'token': TOKEN, 
        'limit': 1000, 
        'filter': 'visible' 
    }
    
    all_cards = []
    last_id = None
    
    url_lists = f"https://api.trello.com/1/boards/{BOARD_ID}/lists"
    url_cards = f"https://api.trello.com/1/boards/{BOARD_ID}/cards"

    try:
        # 3. Puxando as Listas (Tradução de IDs para Nomes)
        resp_lists = requests.get(url_lists, params={'key': API_KEY, 'token': TOKEN})
        mapa_listas = {}
        if resp_lists.status_code == 200:
            listas = resp_lists.json()
            mapa_listas = {lista['id']: lista['name'] for lista in listas}
        else:
            print(f"⚠️ Aviso: Erro {resp_lists.status_code} ao buscar listas.")

        # 4. Loop de Paginação (Lote por Lote)
        while True:
            if last_id:
                params['before'] = last_id
            
            response = requests.get(url_cards, params=params)
            
            if response.status_code != 200:
                print(f"❌ Erro na extração: {response.status_code}")
                print(f"Detalhe: {response.text}")
                break
                
            batch = response.json()
            if not batch:
                break
                
            all_cards.extend(batch)
            last_id = batch[-1]['id'] # Pega o último ID para a próxima página
            
            print(f"🔄 Progresso: {len(all_cards)} cartões capturados...")

            if len(batch) < 1000:
                break

        # 5. Garantindo que não há duplicados por ID e injetando nome da lista
        # Usamos um dicionário para garantir que cada ID apareça apenas uma vez
        dict_unicos = {c['id']: c for c in all_cards}
        
        cards_finais = []
        for c_id, cartao in dict_unicos.items():
            cartao['nome_lista'] = mapa_listas.get(cartao['idList'], 'Desconhecida')
            cards_finais.append(cartao)

        print(f"✅ Extração concluída com sucesso: {len(cards_finais)} cartões únicos e visíveis!")
        return cards_finais

    except Exception as e:
        print(f"❌ Erro inesperado na extração: {e}")
        return []