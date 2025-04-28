anoAtual = 2018
maioresDeIdade = 0
menoresDeIdade = 0

for c in range(7):
    anoNas = int(input(f'Digite o ano de nascimento da {c+1}º pessoa '))
    if (anoAtual - anoNas) >= 18:
        maioresDeIdade += 1
    else: menoresDeIdade += 1
print(f'{maioresDeIdade} pessoas tem MAIS de 18 anos')
print(f'{menoresDeIdade} pessoas tem MENOS de 18 anos')