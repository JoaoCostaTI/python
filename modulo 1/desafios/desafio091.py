from random import randint
from time import sleep
from operator import itemgetter
jogo = {
    'jogador1': randint(1,6),
    'jogador2': randint(1,6),
    'jogador3': randint(1,6),
    'jogador4': randint(1,6)
}
ranking = {}

print('Valores sorteados: ')

for k, v in jogo.items():
    print(f'{k} tirou o valor {v} no dado. ')
    sleep(0.5)
print('=-'*30)
print('== RANKING DOS JOGADORES ==')
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
for k, v in enumerate(ranking):
    print(f'  -{k+1}º lugar {v[0]} com {v[1]}.')
    sleep(0.5)