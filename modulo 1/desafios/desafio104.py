def leiaInt(nInterno):
    valor = input(nInterno)
    while valor.isnumeric() == False:
        print('ERRO! Digite um número inteiro VÁLIDO! ')
        valor = input(nInterno)
    return valor

nGlobal = leiaInt('Digite um numero: ')
print(f'Você acabou de digitar o numero {nGlobal}')