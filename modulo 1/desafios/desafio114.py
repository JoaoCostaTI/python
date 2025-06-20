def verificar_site(url):
    try:
        from urllib.request import urlopen
        resposta = urlopen(url, timeout=5)
        print(f'O site {url} está disponível! Código: {resposta.status}')
    except:
        print(f'Não foi possível acessar o site {url}.')

# Exemplo de uso

# Exemplo de uso
verificar_site('https://www.pudim.com.br/')
