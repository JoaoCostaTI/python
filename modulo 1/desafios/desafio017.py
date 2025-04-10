from math import sqrt, pow

catetoOposto = float(input('Informe o Cateto Oposto: '))
catetoAdjacente = float(input('Informe o Cateto Adjacente: '))

hipotenusa = sqrt((pow(catetoOposto, 2) + pow(catetoAdjacente, 2)))

print(f'O Comprimento da hipotenusa é: {hipotenusa:.2f}')