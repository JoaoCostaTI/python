
somaIdades = 0

homemMaisVelho = ''
idadeHomemMaisVelho = 0

mulheresMenos20 = 20
qtdMulheresMenos20 = 0

for c in range(4):
    print(f'*****{c+1}º PESSOA*****')
    nome = input('Nome: ')
    idade = int(input('Idade: '))
    sexo = input('Sexo [f] ou [m]')

    #Somando as idades para determinar a média de idades
    somaIdades += idade

    #Verificando qual é o homem mais velho
    if sexo == 'm':
        if idade >= idadeHomemMaisVelho:
            homemMaisVelho = nome

    #Verificando quantas mulheres possuem 20 anos
    if sexo == 'f':
        if idade < mulheresMenos20:
            qtdMulheresMenos20 += 1

mediaIdades = somaIdades / 4

print(f'A média das idades é: {mediaIdades}')
print(f'O nome do homem mais velho é: {homemMaisVelho}')
print(f'A quantidade de mulheres com menos de 20 anos é: {qtdMulheresMenos20}')
    