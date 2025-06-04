from random import randint
from time import sleep

numeros = []

def sorteia():
    print('Sorteando 5 numeros da lista: ', end=" ")
    for c in range(5):
        numeros.append(randint(0,10))
    for v in numeros:
        print(f'{v}', end="..." ,flush=True)
        sleep(0.5)
    print()

def somaPar():
    somaPares = 0
    print(f'Somando os valores pares de {numeros}, temos', end=" ")
    for i, v in enumerate(numeros):
        if v % 2 == 0:
            somaPares += v
    print(somaPares)

sorteia()
somaPar()
