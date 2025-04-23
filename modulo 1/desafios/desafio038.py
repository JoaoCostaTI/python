n1 = int(input('Digite um numero: '))
n2 = int(input('Digite outro numero: '))

if n1 > n2:
    print(f'O primeiro valor {n1} é maior que {n2}')
elif n1 == n2:
    print(f'{n1} é igual a {n2} portanto não existe maior ou menor')
else:
    print(f'O Segundo valor {n2} é maior que {n1}')