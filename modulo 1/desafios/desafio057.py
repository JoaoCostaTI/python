sexo = ''

while sexo != 'M' and sexo != 'F':
    sexo = str(input('Qual o sexo? '))
    if sexo != 'M' and sexo != 'F':
        print('Incorreto! Escolha entre [M \ F]')
print('FIM do programa!')