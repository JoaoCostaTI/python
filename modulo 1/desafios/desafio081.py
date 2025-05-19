numeros = []

qtdNumeros = 0
op = ''

while True:
    #Lendo os numeros
    n = int(input('Digite um numero: '))

    #Adicionando os numeros na lista:
    numeros.append(n)

    #Contando quantidade de numeros digitados
    qtdNumeros += 1

    #Verificando se deseja continuar:
    op = str(input('Deseja continuar? [S/N]')).upper().strip()
    if op == 'N':
        print('Saindo do programa...')
        break


#Mostrando quantidade de numeros digitados
print(f'Foram digitados {qtdNumeros} numeros')

#Mostrando a lista em forma decrescente
numeros.sort(reverse=True)
print(f'Lista com os numeros em decrescente: {numeros}')

#Verificando se o valor 5 está ou não na lista:
num = 5
for indice, valor in enumerate(numeros):
    if num == valor:
        print(f'O Valor {num} foi encontrado na posição: {indice}')
if num not in numeros:
    print(f'O valor {num} não foi encontrado na lista')