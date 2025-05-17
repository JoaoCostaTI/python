numeros = []

maior = 0
menor = 0

for c in range(5):
    #Inserindo os numeros na lista
    n = int(input(f'Digite o valor para posição [{c}]: '))
    numeros.append(n)
    if c == 0:
        maior = menor = numeros[c]
    else:
        if numeros[c] > maior:
            maior = numeros[c]
        if numeros[c] < menor:
            menor = numeros[c]


print(f'Você digitou os valores: {numeros}')

print(f'O maior valor digitado é: {maior}, nas posições: ', end="")
for indice, valor in enumerate(numeros):
    if valor == maior:
        print(f'{indice}...', end="")
print()
    
print(f'O menor valor digitado é: {menor} nas posições: ', end="" )
for indice, valor in enumerate(numeros):
    if valor == menor:
        print(f'{indice}...', end="")
print()