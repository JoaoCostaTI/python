nome = input('Digite seu nome: ')
nomeSemEspaco = nome.replace(" ", "")
nomeFatiado = nome.split()

print(f'Nome com todas as letras maiusculas: {nome.upper()}\nNome do todas letras minúsculas: {nome.lower()}\nQuantidade de letras ao todo(Sem Espaços): {len(nomeSemEspaco)}\nQuantidade de letras do primeiro nome: {len(nomeFatiado[0])}')