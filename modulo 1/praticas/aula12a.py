nome = str(input('Qual é seu nome: '))

if nome == 'joao':
    print('Que nome lindo! ')
elif nome == 'pedro' or nome == 'maria' or nome == 'paulo':
    print('Seu nome é bem popular no Brasil! ')
elif nome in 'ana claudia pessica juliana':
    print('Belo nome feminino! ')
print(f'Tenha um bom dia, {nome}! ')