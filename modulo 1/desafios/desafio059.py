n1 = int(input('Digite um numero: '))
n2 = int(input('Digite outro numero: '))

menu = 0

while menu != 6:
    menu = int(input('Selecione a opção: \n[1]-Somar\n[2]-Multiplicar\n[3]-Maior\n[4]-Novos Numeros\n[5]-Sair do programa '))

    if menu == 5:
        print('Saindo do Programa...')
        break
    if menu == 1:
        op = n1 + n2
        print(f'{n1} + {n2} = {op}')

    if menu == 2:
        op = n1 * n2
        print(f'{n1} x {n2} = {op}')

    if menu == 3:
        if n1 == n2:
            print(f'{n2} É IGUAL a {n2}')
        if n1 > n2:
            print(f'{n1} é MAIOR que {n2}')
        if n1 < n2: 
            print(f'{n2} é MAIOR que {n1}')
        
    if menu >= 6:
        print('Opção inválida! Selecione uma opção correta! ')
        
    if menu == 4:
        print('Selecionar novos numeros!')
        n1 = float(input('Digite um numero: '))
        n2 = float(input('Digite outro numero: '))

print('Fim do Programa! ')