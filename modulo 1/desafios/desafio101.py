

def voto(anoNascimento):
    from datetime import date

    anoAtual = date.today().year
    idade = anoAtual - anoNascimento

    if idade > 65:
        return f'Com {idade} anos: VOTO OPCIONAL! '
    elif idade >= 18:
        return f'Com {idade} anos: VOTO OBRIGATÓRIO.'
    else:
        return f'Com {idade} anos: NÃO VOTA.'

print('-' * 30)
ano = int(input('Em que ano você nasceu? '))
print(voto(ano))