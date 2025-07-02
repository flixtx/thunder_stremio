import requests
from urllib.parse import urlparse, parse_qs

api = 'https://kim.nl.tab.digital/s/t5fYJ49CZKkfnZa/download/listas.txt\'

def convert_to_json(url):
    """
    Converte uma URL de IPTV em um dicionário JSON.
    """
    parsed_url = urlparse(url)
    host = parsed_url.scheme + '://' + parsed_url.netloc
    port = parsed_url.port if parsed_url.port else 80
    query_params = parse_qs(parsed_url.query)
    
    # Extrai username e password dos parâmetros
    username = query_params.get('username', [None])[0]
    password = query_params.get('password', [None])[0]
    
    # Cria o dicionário JSON
    json_data = {
        "BaseURL": host + ':' + str(port),
        "username": username,
        "password": password
    }
    
    return json_data

def total_servers():
    servers_ = []
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    response = requests.get(api, headers=headers)
    if response.status_code == 200:
        src = response.text
        lines = src.splitlines()
        for line in lines:
            # Extrai a URL do servidor
            url = line.strip()
            # Converte a URL em JSON
            json_data = convert_to_json(url)
            servers_.append(json_data)
    return len(servers_)    


def select_server(server=None):
    servers_ = []
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    response = requests.get(api, headers=headers)
    if response.status_code == 200:
        src = response.text
        lines = src.splitlines()
        for line in lines:
            # Extrai a URL do servidor
            url = line.strip()
            # Converte a URL em JSON
            json_data = convert_to_json(url)
            servers_.append(json_data)
    else:
        print(f"Erro ao acessar a URL: {response.status_code}")
    if server or server == 0:
        try:
            select = servers_[int(server)]
        except IndexError:
            try:
                select = servers_[0]
            except IndexError:
                select = []
    else:
        select = []
    return select

# print(select_server(0))
