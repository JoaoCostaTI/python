jogador = {}
partidas = []

jogador['nome'] = str(input('Nome: '))
tot = int(input(f'Quantas partidas jogou {jogador["nome"]}: '))

for c in range(tot):
    partidas.append(int(input(f"   Quantos gols na partida {c}? ")))
jogador['gols'] = partidas[:]
jogador['total'] = sum(partidas)

print('=-' * 30)
print(jogador)
print('=-' * 30)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}')
print('=-' * 30)
print(f'O jogador {jogador["nome"]} jogou {len(partidas)} partidas')
print('=-' * 30)
for i, v in enumerate(jogador['gols']):
    print(f'   => Na partida {i}, fez {v} gols.')
print(f'Total de {sum(jogador['gols'])} gols.')
