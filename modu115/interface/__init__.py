def leiaInt(msg):
    while True:
        try: 
            n = input(msg)
            return int(n)
        except KeyboardInterrupt:
            print(f'\nUsuário preferiu não informar os dados.')
            return 0
        except ValueError:
            print(f'ERRO! Por favor, repita e digite um valor inteiro VÁLIDO!')

def linha(tam = 42):
    return '-' * tam

def cabecalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())

def menu(lista):
    c = 1
    for i in lista:
        print(f'\033[33m{c}\033[m - \033[34m{i}\033[m')
        c += 1
    print(linha())
    opc = leiaInt('Sua opção: ')
    return opc
