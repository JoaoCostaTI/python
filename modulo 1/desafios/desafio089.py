
dados = []
alunos = []

while True:
    #Coletando os dados:
    dados.append(str(input('Nome: ')))
    dados.append(float(input('Nota 1: ')))
    dados.append(float(input('Nota 2: ')))
    media = (dados[1] + dados[2]) / 2
    dados.append(media)

    #Colocando os dados em alunos na lista final
    alunos.append(dados[:])
    dados.clear()

    op = str(input('Deseja continuar? [S/N]: ')).upper().strip()

    if op in 'N':
        break
print(15*'-=')
print(f'{'No.':<4}{'NOME':<15}{'MÉDIA':<6}')
print(10*'---')
for indice, inf in enumerate(alunos):
    print(f'{indice:<4}{inf[0]:<15}{inf[3]:>6.1f}')

while True:
    chave = int(input('Mostrar notas de qual aluno? (999 interrompe): '))

    for indice, inf in enumerate(alunos):
        if indice == chave:
            print(f'Notas de {inf[0]} são {inf[1], inf[2]}')
    print(10*'---')
    if chave == 999:
        print('Saindo do programa...')
        break