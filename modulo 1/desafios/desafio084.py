from time import sleep

pessoas = []
dados = []

pesadas = []
leves = []

qtdPessoas = 0

while True:
    #Pedindo o nome
    nome = str(input('Digite o nome: '))
    pessoas.append(nome)

    #pedindo o peso
    peso = float(input('Digite o peso: '))
    pessoas.append(peso)

    #Calculando quantidade de pessoas cadastradas
    qtdPessoas += 1

    #Jogando os dados das pessoas para serem analisadas:
    dados.append(pessoas[:])

    #Limpando os dados para não copiar sempre
    pessoas.clear()

    sleep(0.5)
    print('Cadastrado com sucesso...')
    op = str(input('Deseja continuar cadastrando? [S/N]')).upper().strip()


    if op in 'N':
        print('*-' * 12)
        sleep(0.5)
        print('Saindo do programa...')
        break

#Verificando as pessoas MAIS e MENOS Pesadas
maiorPeso = 0
menorPeso = 99999

for nome, peso in dados:
    if peso >= maiorPeso:
        maiorPeso = peso
        pesadas.append(nome)
    elif peso <= menorPeso:
        menorPeso = peso
        leves.append(nome)



#Mostrando quantas pessoas foram cadastradas:
sleep(0.5)
print('*-' * 12)
print(f'Foram cadastradas {qtdPessoas} pessoas')
sleep(0.5)
print(f'O maior peso foi: {maiorPeso}, e as pessoas são: {pesadas}')
sleep(0.5)
print(f'O menor peso foi: {menorPeso}, e as pessoas são: {leves}')
sleep(0.5)
print('Saindo do programa...')

    