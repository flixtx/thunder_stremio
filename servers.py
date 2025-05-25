import requests
from urllib.parse import urlparse, parse_qs

api = '\x68\x74\x74\x70\x73\x3a\x2f\x2f\x64\x72\x69\x76\x65\x2e\x67\x6f\x6f\x67\x6c\x65\x2e\x63\x6f\x6d\x2f\x75\x63\x3f\x65\x78\x70\x6f\x72\x74\x3d\x64\x6f\x77\x6e\x6c\x6f\x61\x64\x26\x69\x64\x3d\x31\x49\x45\x70\x6a\x41\x30\x38\x72\x61\x63\x4c\x6b\x6b\x52\x4f\x76\x6b\x37\x47\x47\x48\x42\x54\x43\x30\x71\x6c\x66\x48\x4e\x4e\x6a'

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
