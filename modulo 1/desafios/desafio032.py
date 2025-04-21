from datetime import date

ano = int(input('Informe um ano a ser analisado: [0] Para analisar o ano atual '))

if ano == 0:
    ano = date.today().year

if ano % 4 == 0 and (ano % 100 != 0 or ano % 400 == 0):
    print(f'Ano de {ano} Bissexto')
else:
    print(f'Ano de {ano} NAO Bissexto')