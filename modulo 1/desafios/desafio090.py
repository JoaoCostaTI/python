dados = {

}

nome = str(input('Nome: '))
dados['Nome'] = nome
media = float(input(f'Média de {nome}: '))
dados['Media'] = media

print('-=' * 15)

if dados['Media'] >= 7:
    dados['Situacao'] = 'Aluno Aprovado!'
else:
    if dados['Media'] >= 6: 
        dados['Situacao'] = 'Aluno Recuperação'
    else:
        dados['Situacao'] = 'Aluno Reprovado'

for key, valor in dados.items():
    print(f'{key} é igual a {valor}')
    
