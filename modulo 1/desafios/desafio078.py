numeros = []

for c in range(5):
    #Lendo os numeros
    n = int(input('Digite um numero: '))

    #Guardando os numeros
    numeros.append(n)

    #Verificando qual é o maior e o menor
    if c == 0:
        maior = menor = n
    if n > maior:
        maior = n
    if n < menor:
        menor = n
#Mostrando a lista completa
print(f'Lista completa: {numeros}')

#Mostrando apenas os INDICES do NUMERO MAIOR
print(f'Maior numero = {maior}', end=" nos indices: ")
for indice, valores in enumerate(numeros):
    if valores == maior:
        print(f'{indice}...', end="")

#Mostrando os INDICES do NUMERO MENOR
print(f'\nMenor numero = {menor}', end=" nos indices: ")
for indice, valores in enumerate(numeros):
    if valores == menor:
        print(f'{indice}...', end="")
 