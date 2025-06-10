from time import sleep

while True:
    print('\033[32m' + '~' * 30)
    print(f'{"Sistema de Ajuda PyHelp".center(30)}')
    print('~' * 30 + '\033[m')

    sleep(1)

    op = str(input('Função ou Biblioteca > ')).strip().lower()

    sleep(1)

    if op == 'fim':
        print('~' * 30)
        print('Até Logo!'.center(30))
        print('~' * 30)
        break
    else: 
        print('\033[32m' + '~' * 45)
        print(f'Acessando o manual do comando {op}'.center(45))
        print('~' * 45 + '\033[m')

        sleep(1)
        help(op)
   

    