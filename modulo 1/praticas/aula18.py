galera = list()
dado = list()
totalMaior = totalMenor = 0

for c in range(3):
    #Pedindo o nome
    nome = str(input('Digite seu nome: '))
    dado.append(nome)

    #pedindo a idade
    dado.append(int(input('Digite a idade: ')))

    #Jogando os dados dentro de galera
    galera.append(dado[:])
    dado.clear()

for p in galera:
    if p[1] >= 21:
        print(f'{p[0]} tem mais de 21 anos...')
        totalMaior += 1
    else:
        print(f'{p[0]} tem menos de 21 anos...')
        totalMenor += 1

print(f'{totalMaior} pessoas são maiores de idade...')
print(f'{totalMenor} pessoas são menores de idade...')