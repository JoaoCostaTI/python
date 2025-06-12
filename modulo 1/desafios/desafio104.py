def leiaInt(msg):
    ok = False
    valor = 0

    while True:
        num = str(input(msg))

        if num.isnumeric():
            valor = int(num)
            ok = True
        else:
            print('ERRO! Digite um valor válido! ')
        if ok:
            break
    return valor

n = leiaInt('Digite um numero: ')
print(f'Você digitou o numero {n}')