'''r = 'S'
contagem = 0

while r == 'S':
    n = int(input('Digite um valor: '))
    contagem += n
    r = str(input('Deseja continuar? [S] ou [N]')).upper()

print(f'Total {contagem}')
print('FIM')'''

n = 1 
pares = 0
impares = 0

while n != 0:
    n = int(input('Digite um valor: '))
    if n != 0: 
        if n % 2 == 0:
            pares += 1
            print(f'O número {n} é par')
        else:
            impares += 1
            print(f'O numero {n} é ímpar')
print(f'Neste contador temos {pares} numeros pares e {impares} numeros impares')
print('FIM')