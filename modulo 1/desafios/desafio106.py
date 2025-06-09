from time import sleep

while True:
    print('\033[32m' + '~' * 30)
    print(f'{"Sistema de Ajuda PyHelp".center(30)}')
    print('~' * 30 + '\033[m')

    sleep(1)

    op = str(input('Função ou Biblioteca > '))

    sleep(1)

    print('\033[32m' + '~' * 45)
    print(f'Acessando o manual do comando {op}'.center(45))
    print('~' * 45 + '\033[m')

    sleep(1)

    ajuda = help(op)

    sleep(1)

    print(ajuda)

    