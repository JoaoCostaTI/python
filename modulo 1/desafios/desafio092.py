#Aposentar com 35 anos

dados = {}


dados['nome'] = str(input('Nome: '))

idade = int(input('Ano de nascimento: '))
idadeReal = 2025 - idade
dados['idade'] = idadeReal

dados['ctps'] = int(input('Carteira de trabalho (0 não tem): '))

dados['contracacao'] = int(input('Ano de contratação: '))
dados['salario'] = float(input('Salário: R$ '))

print(dados)