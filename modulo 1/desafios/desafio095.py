jogador = {}
jogadores = []
listaGols = []

while True:
    jogador['nome'] = str(input('Nome do Jogador: '))
    qtdPartidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    totalGols = 0

    for c in range(qtdPartidas):
        gols = int(input(f'Quantos gols na partida {c}? '))
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
        print('Saindo do programa...')
        break

    while dadosJogador >= len(jogadores):
        print(f'ERRO! Não existe jogador com código {dadosJogador}! Tente novamente...')

        dadosJogador = int(input('Mostrar dados de qual jogador? (999 para sair)... '))

        if dadosJogador == 999:
            break

    if dadosJogador == 999:
        print('Saindo do programa...')
        break

    print(f'--- LEVANTAMENTO DO JOGADOR {jogadores[dadosJogador]["nome"]}: ')
    for c in range(len(jogadores[dadosJogador]['gols'])):
        print(f'{"No":>6} jogo {c} fez {jogadores[dadosJogador]["gols"][c]} gols. ')
