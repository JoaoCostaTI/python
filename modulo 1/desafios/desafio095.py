jogador = {}
jogadores = []
listaGols = []

while True:
    jogador['nome'] = str(input('Nome do Jogador: '))
    qtdPartidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    totalGols = 0

    for c in range(qtdPartidas):
        gols = int(input(f'Quantos gols na partida {c+1}? '))
        totalGols += gols
        listaGols.append(gols)

    jogador["gols"] = listaGols[:]
    jogador["total"] = totalGols

    #Adicionando os jogadores em uma lista com todos jogadores
    jogadores.append(jogador.copy())
    listaGols.clear()

    op = str(input('Quer continuar? [S/N]')).upper().strip()
    if op in 'N':
        break

print('-=' * 30)
print(f'{"Cod"} {"nome":<15} {"gols":<15} {"total"}')
print('-'*60)
#Listagem com os jogadores: 
for i, v in enumerate(jogadores):
    print(f'{i:<4}{v["nome"]:<16}{str(v["gols"]):<16}{v["total"]}')

while True:
    dadosJogador = int(input('Mostrar dados de qual jogador? (999 para sair)... '))
    if dadosJogador == 999:
        break
    if dadosJogador >= len(jogadores):
        print(f'ERRO, não existe jogador com código {dadosJogador}! ')
    else:
        print(f'Levantamento do jogador {jogadores[dadosJogador]["nome"]}: ')
        for i, g in enumerate(jogadores[dadosJogador]['gols']):
            print(f'   Na partida {i+1} fez {g} gols...')
    print('-=' * 30)
print('Volte sempre!!!')    
