reta1 = float(input('Comprimento da primeira reta: '))
reta2 = float(input('Comprimento da segunda reta: '))
reta3 = float(input('Comprimento da terceira reta: '))

if reta1 + reta2 > reta3 and reta1 + reta3 > reta2 and reta2 + reta3 > reta1:
    print('Pode formar um triangulo! ')
    if reta1 == reta2 and reta1 == reta3:
        print('Forma-se Triangulo Equilátero com Todos lados iguais! ')
    elif reta1 == reta2 or reta2 == reta3 or reta1 == reta3:
        print('Forma-se um Triangulo Isósceles! Apenas 2 lados iguais! ')
    else: print('Forma-se um triangulo Escaleno, Todos os lados diferentes! ')
else:
    print('Não pode formar um triangulo! ')
