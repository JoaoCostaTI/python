valores = []
op = ''

while True:
    n = int(input('Digite um numero: '))

    if n not in valores:
        print('Valor adicionado com sucesso...')
        valores.append(n)
    else:
        print('Valor já existe, não será adicionado...')
    
    op = str(input('Deseja continuar? [S/N] ')).upper().strip()

    if op == 'N':
        break

#Ordenando a lista
valores.sort()
print(f'Lista completa ordenada {valores}')