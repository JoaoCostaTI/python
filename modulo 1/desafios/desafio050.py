
somaPares = 0

for c in range(0,6):
    n = int(input('Digite um numero: '))
    
    if n % 2 == 0:
        print(f'O numero {n} é par, foi adicionado a soma! ')
        somaPares = somaPares + n
    else: print(f'O numero {n} é ímpar, não foi adicionado a soma! ')
print(f'A Soma total dos numeros pares deu: {somaPares}')