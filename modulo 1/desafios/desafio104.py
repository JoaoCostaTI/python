def leiaInt(nInterno):
    valor = input(nInterno)
    
    while not valor.isnumeric():
        print('ERRO, Digite um numero válido!')
        valor = input(nInterno)
    
    return int(valor)

nGlobal = leiaInt('Digite um numero: ')
print(f'Você acabou de digitar o numero {nGlobal}')