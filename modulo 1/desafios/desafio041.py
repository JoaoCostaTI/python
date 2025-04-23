anoNascimento = int(input('Digite o seu ano de nascimento: '))
anoAtual = 2025
idade = anoAtual - anoNascimento

if idade <= 9:
    print(f'{idade} Categoria MIRIM!')
elif idade > 9  and idade <= 14:
    print(f'{idade} Categoria INFANTIL!')
elif idade > 14 and idade <= 19:
    print(f'{idade} Categoria JUNIOR!')
elif idade == 20:
    print(f'{idade} Categoria SENIOR!')
else: print(f'{idade} Categoria MASTER!')