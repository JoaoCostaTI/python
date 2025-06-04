time = {

}

tabelaCampeonato = []

for c in range(1):
    time['nome'] = str(input('Nome: '))
    time['P'] = int(input('Pontos: '))
    time['J'] = int(input('Jogos: '))
    time['V'] = int(input('Vitórias: '))
    time['E'] = int(input('Empates: '))
    time['D'] = int(input('Derrotas: '))

    tabelaCampeonato.append(time.copy())
    time.clear()

print(f'<<<Tabela Campeonato Fulero>>>'.center(33))
print(f'{"Time":<15}{"P":<3} {"J":<3} {"V":<3} {"E":<3} {"D":<3}')

for i, v in enumerate(tabelaCampeonato):
    print(f'.{tabelaCampeonato[i]["nome"]:<13} {tabelaCampeonato[i]["P"]:<3} {tabelaCampeonato[i]["J"]:<3} {tabelaCampeonato[i]["V"]:<3} {tabelaCampeonato[i]["E"]:<3} {tabelaCampeonato[i]["D"]:<3}')




