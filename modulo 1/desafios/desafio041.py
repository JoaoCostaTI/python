anoNascimento = int(input('Digite o seu ano de nascimento: '))
anoAtual = 2017
idade = anoAtual - anoNascimento

if idade <= 9:
    print(f'Você tem {idade} anos\nCategoria MIRIM!')
elif idade > 9  and idade <= 14:
    print(f'Você tem {idade} anos\nCategoria INFANTIL!')
elif idade > 14 and idade <= 19:
    print(f'Você tem {idade} anos\nCategoria JUNIOR!')
elif idade <= 25:
    print(f'Você tem {idade} anos\nCategoria SENIOR!')
else: print(f'Você tem {idade} anos\nCategoria MASTER!')