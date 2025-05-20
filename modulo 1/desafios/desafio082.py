numeros = []
listaPar = []
listaImpar = []

while True:
    #Entrada dos dados
    n = int(input('Digite um numero: '))

    #Adicionando na lista
    numeros.append(n)

    #Continuar ou não
    op = str(input('Deseja continuar? [S/N] ')).upper().strip()

    if op == 'N':
        break

#Separando lista par e impar
for c in numeros:
    if c % 2 == 0:
        listaPar.append(c)
    else:
        listaImpar.append(c)

#Resultados
print("-=" * 30)
print(f'Lista completa: {numeros}')
print(f'Lista somente com PARES: {listaPar}')
print(f'Lista somente com IMPARES: {listaImpar}')
