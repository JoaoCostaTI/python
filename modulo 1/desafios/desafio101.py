def voto(anoNascimento):
    idade = 2018 - anoNascimento

    if idade > 65:
        print(f'Com {idade} anos: VOTO OPCIONAL! ')
    elif idade >= 18:
        print(f'Com {idade} anos: VOTO OBRIGATÓRIO.')
    else:
        print(f'Com {idade} anos: NÃO VOTA.')

print('-' * 30)
ano = int(input('Em que ano você nasceu? '))
voto(ano)