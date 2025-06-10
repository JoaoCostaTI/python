dados = {}
notas = []

nome = str(input('Nome do Aluno: '))

nota1 = float(input('Nota 1: '))
notas.append(nota1)
nota2 = float(input('Nota 2: '))
notas.append(nota2)

media = (nota1+nota2) / 2

dados['nome'] = nome
dados['notas'] = notas.copy()
notas.clear()
dados['media'] =  media

print(dados)

for k, v in dados.items():
    print(f'{k} é: {v}')