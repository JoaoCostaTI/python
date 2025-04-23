n1 = float(input('Digite a nota 1: '))
n2 = float(input('Digite a nota 2: '))

media = (n1 + n2) / 2

if media < 5.0:
    print(f'REPROVADO! Sua média final ficou: {media:.1f}')
elif media > 4.9 and media < 7:
    print(f'RECUPERAÇÃO! Sua média final ficou: {media:.1f}')
else:
    print(f'APROVADO! Sua média final ficou: {media:.1f} ')