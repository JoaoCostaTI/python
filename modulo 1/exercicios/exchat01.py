aluno = {}

aluno['nome'] = str(input('Nome do aluno: '))
aluno['nota'] = float(input(f'Nota de {aluno["nome"]}: '))

if aluno['nota'] >= 7:
    aluno['situacao'] = 'aprovado'
elif aluno['nota'] >= 5:
    aluno['situacao'] = 'recuperacao'
else:
    aluno['situacao'] = 'reprovado'

for k, v in aluno.items():
    print(f'{k.capitalize()}: {v}')