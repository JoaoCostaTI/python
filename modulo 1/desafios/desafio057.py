'''
sexo = ''

while sexo != 'M' and sexo != 'F':
    sexo = str(input('Qual o sexo? ')).strip().upper()[0]
    if sexo != 'M' and sexo != 'F':
        print('Incorreto! Escolha entre [M / F]')
    if sexo == 'M':
        print('Sexo MASCULINO selecionado! ')
    if sexo == 'F':
        print('Sexo FEMININO selecionado! ')
print('FIM do programa!')
'''

sexo = str(input('Digite seu sexo: [M / F]')).strip().upper()[0]

while sexo not in 'MmfF':
    sexo = str(input('Opção inválida! Digite novamente seu sexo: [M/F]')).strip().upper()[0]
print(f'Sexo {sexo} selecionado com sucesso!')