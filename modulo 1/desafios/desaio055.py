maiorPeso = 0
menorPeso = 1000

for c in range(5):
    peso = float(input(f'Digite o peso da {c+1}º pessoa: '))
    if peso > maiorPeso:
        maiorPeso = peso
    if peso < menorPeso:
        menorPeso = peso
print(f'Maior peso = {maiorPeso}')
print(f'Maior peso = {menorPeso}')