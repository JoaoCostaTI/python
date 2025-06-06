dados = {}
alunos = []
notas = []

def escopoBoletim():
    msg = 'BOLETIM ESCOLAR'
    tam = len(msg) + 10
    print('~' * tam)
    print(f'{msg.center(tam)}')
    print('~' * tam)
    print(f'{"No.":<5}{"Nome":<15}{"Média"}')

while True: 
    nota1 = 0
    nota2 = 0
    
    #Dados + Notas
    dados['nome'] =  str(input('Nome do aluno: '))
    nota1 = float(input('Nota 1: '))
    notas.append(nota1)
    nota2 = float(input('Nota 2: '))
    notas.append(nota2)
    #Calculando média
    media = (nota1 + nota2) / 2
    #Adicionando no dicionário as notas que estão em uma lista
    dados['notas'] = notas[:]
    notas.clear()

    dados['media'] = media

    alunos.append(dados.copy())
    dados.clear()

    while True:
        op = str(input('Deseja continuar? [S/N] ')).strip().upper()

        if op in ["S", "N"]:
            break
        else:
            print('Opção inválida. Digite apenas S ou N. ')
    if op == 'N':
        print('Saindo do cadastro de alunos...')
        break


escopoBoletim()
for i, v in enumerate(alunos):
    print(f'{i:<5}{v["nome"]:<15}{v["media"]}')

while True:
    dadosAluno = int(input('Mostrar dados de qual aluno? (999) para sair: '))

    if dadosAluno == 999:
        print('Saindo do programa...')
        break
    if dadosAluno >= len(alunos):
        print(f'Não existe aluno com o código {dadosAluno}')
    else:
        aluno = alunos[dadosAluno]
        print(f'Notas de {aluno["nome"]}: {aluno["notas"]}')
        