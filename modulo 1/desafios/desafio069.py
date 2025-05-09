pessoas18Mais = 0
homens = 0
mulheres20Menos = 0

while True:
    print(10*"-+")
    print('CADASTRO DE PESSOA: ')
    print(10*"-+")
    idade = int(input('Digite sua idade: '))
    sexo = str(input('Digite seu sexo: [M/F]')).strip().upper()
    continuar = str(input('Deseja continuar? [S/N]')).strip().upper()

    #Calculando Quantas pessoas tem mais de 18 anos:
    if idade >= 18:
        pessoas18Mais += 1

    #Calculando quantos homens foram cadastrados:
    if sexo == 'M':
        homens += 1
    
    #calculando quantas mulheres tem menos de 20 anos:
    if sexo == 'F' and idade <= 20:
        mulheres20Menos += 1
    
    if continuar == 'N':
        break

print(18*"-+")
print(f'Temos {pessoas18Mais} pessoas com mais de 18 anos...')
print(f'Temos {homens} homens cadastrados...')
print(f'Temos {mulheres20Menos} mulheres com menos de 20 anos...')
print(18*"-+")

