n = int(input('Digite um numero: '))
qtdPrimo = 0

for c in range(1, n+1):
    if n % c == 0:
        qtdPrimo += 1
if qtdPrimo > 2:
    print(f'{n} NÃO é numero primo! ')
else:
    print(f'{n} É sim numero primo! ')