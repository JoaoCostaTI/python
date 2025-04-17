n1 = int(input('Informe um numero: '))
n2 = int(input('Informe outro numero: '))
n3 = int(input('Informe outro numero: '))

lista = [n1,n2,n3]
lista.sort()

print(f'O maior numero é: {lista[2]}\nO numero do meio é: {lista[1]}\nO menor numero é: {lista[0]}')
