#Aposentar com 35 anos

dados = {}
n_aposentadoria = 35

dados['nome'] = str(input('Nome: '))

idade = int(input('Ano de nascimento: '))
idadeReal = 2025 - idade
dados['idade'] = idadeReal

dados['ctps'] = int(input('Carteira de trabalho (0 não tem): '))

if dados['ctps'] != 0:
    dados['contracacao'] = int(input('Ano de contratação: '))

    dados['salario'] = float(input('Salário: R$ '))

    #calculando quando irá se aposentar
    dados['aposentadoria'] = (dados['contracacao'] + n_aposentadoria) - idade

print('-=' * 30)
print(dados)

for k, v in dados.items():
    print(f'{k} tem o valor: {v}')