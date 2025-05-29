jogador = {}
listaGols = []

#Nome do jogador
jogador['nome'] = str(input('Nome do jogador: '))

#Calculando quantidades de partida para utilizar no For e calcular quantidade de gols
nPartidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))

#Calculando quantidade de gols
totalGols = 0
for c in range(nPartidas):
    gols = int(input(f'Quantos gols na partida {c}? '))
    #Adicionando em uma lista os gols da partida especifica
    listaGols.append(gols)
    #Criando uma lista dentro do dicionário com os gols de cada partida
    jogador['gols'] = listaGols.copy()
    #Somando a quantidade de gols
    totalGols += gols
#Adicionando o total de gols no dicionário jogador 
jogador['total'] = totalGols
#Resultado do dicionário completo
print('=-'*30)
print(jogador)
print('=-'*30)
#Resultado do que tem em cada campo
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}')
print('=-'*30)

print(f'O jogador {jogador["nome"]} jogou {nPartidas} partidas')

for i, v in enumerate(listaGols):
    print(f'   => Na partida {i}, fez {v} gols.')
print(f'Foi um total de {jogador["total"]} gols. ')
