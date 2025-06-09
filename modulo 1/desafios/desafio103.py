def ficha(nome='<Desconhecido>', gols=0):
    print(f'O Jogador {nome} fez {gols} gols(s) no campeonato')
    print(type(gols))

#Programa Principal
nomeJogador = str(input('Nome do Jogador: '))
golsJogador = str(input('Numero de gols: '))

if golsJogador.isnumeric():
    golsJogador = int(golsJogador)
else:
    golsJogador = 0

if nomeJogador.strip() == '':
    ficha(gols = golsJogador)
else:
    ficha(nomeJogador, golsJogador)

