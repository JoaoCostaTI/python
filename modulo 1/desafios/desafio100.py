from random import randint
from time import sleep

def sorteia(lista):
    print('=' * 30)
    print('Sorteando os 5 numeros: ' ,end="")
    for c in range(5):
        lista.append(randint(1,10))
    for valor in lista:
        print(f'{valor}...', end="")
    print()
def somaPar(lista):
    somaPares = 0
    for v in lista:
        if v % 2 == 0:
            somaPares += v
    print(f'Somando os valores pares de {lista} temos = {somaPares}')

numeros = []
sorteia(numeros)
somaPar(numeros)