pessoas = []
dados = []
maisPesadas = []
maisLeves = []

maiorPeso = menorPeso = 0

contador = 0

while True:
    nome = str(input('Nome: '))
    pessoas.append(nome)

    peso = float(input('Peso: '))
    pessoas.append(peso)

    #Capturando os dados
    dados.append(pessoas[:])

    #Zerando a lista para evitar duplicatas
    pessoas.clear()

    #Verificando maior e menor peso
    if contador == 0:
        maiorPeso = menorPeso = peso
    else:
        if peso >= maiorPeso:
            maiorPeso = peso
        if peso <= menorPeso:
            menorPeso = peso

    #Atualizando Contador
    contador += 1

    op = str(input('Continuar? [S/N]...')).strip().upper()

    if op in 'nN':
        break

#Mostrando pessoas mais pesadas
print(f'Maior Peso = {maiorPeso}', end='Kg ')
for nome, peso in dados:
    if peso == maiorPeso:
        maisPesadas.append(nome)
print(f' nomes = {maisPesadas}')

#Mostrando pessoas mais leves
print(f'Menor Peso = {menorPeso}', end='Kg ')
for nome, peso in dados:
    if peso == menorPeso:
        maisLeves.append(nome)
print(f' nomes = {maisLeves}')

print(f'Foram cadastradas: {len(dados)} pessoas')