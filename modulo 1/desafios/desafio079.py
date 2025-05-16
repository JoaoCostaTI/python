valores = list()

op = ''

while True:
    n = int(input('Digite um numero: '))
    
    #Adicionando o valor na lista APENAS Se ele não estiver dentro da lista
    if n not in valores:
        print('Valor adicionado com Sucesso...')
        valores.append(n)
    else:
        print(f'Valor Duplicado, não vou adicionar...')
    
    #Opção de deseja continuar
    op = str(input('Deseja continuar?[S/N] ')).upper().strip()

    if op == 'N':
        break

valores.sort()

print(f'Todos os valores da lista foram: {valores}')
