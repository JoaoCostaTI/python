n = int(input('Digite um numero: '))

for c in range(1, n-1):
    if n % c == 0:
        print('Não é primo! ')
    else:
        print('é primo! ')