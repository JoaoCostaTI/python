n1 = float(input('Primeira nota: '))
n2 = float(input('Seguda nota: '))
media = (n1 + n2) / 2

print(f'Sua media foi: {media:.1f}')

if media >= 6:
    print('Sua média é boa!')
else:
    print('Sua média foi ruim, estude mais!')