from random import randint
from time import sleep

numeros = []

def sorteia(suaLista):
    print('Sorteando 5 numeros da lista: ', end=" ")
    for c in range(5):
        v = randint(0,10)
        suaLista.append(v)
        print(f'{v}', end="... " ,flush=True)
        sleep(0.5)
    print()
def somaPar(suaLista):
    somaPares = 0
    print(f'Somando os valores pares de {suaLista}, temos', end=" ")
    for v in suaLista:
        if v % 2 == 0:
            somaPares += v
    print(somaPares)
sorteia(numeros)
somaPar(numeros)