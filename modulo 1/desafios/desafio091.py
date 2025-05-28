from random import randint
from time import sleep

resultados = {}


print('Valores sorteados: ')
for c in range(4):
    #Gerando o numero:
    n = randint(1,6)
    sleep(0.7)

    #Resultados
    print(f'   O jogador {c+1} tirou: {n}')
    resultados[f'jogador{c+1}'] = n

sleep(0.7)
print('Ranking dos jogadores: ')

{k: v for k, v in sorted(resultados.items(), key=lambda item: item[1])}

ranking = 1
for jogador in sorted(resultados, key=lambda x: resultados[x], reverse=True):
    sleep(0.7)
    print(f'   {ranking}º Lugar: {jogador} com {resultados[jogador]}')
    ranking+=1