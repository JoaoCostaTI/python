n = int(input('Digite um numero: '))
opcao = int(input('Para qual base deseja converter? \n[1] Binário\n[2] Octal\n[3] Hexadecimal\n'))

if opcao == 1:
    binario = bin(n)[2:]
    print(f'O numero {n} em binário é: {binario}')
elif opcao == 2:
    octal = oct(n)[2:]
    print(f'O numero {n} em Octal é: {octal} ')
elif opcao == 3:
    hexa = hex(n)[2:]
    print(f'O numero {n} em Hexadecimal é: {hexa}')
else:
    print('Opção inválida, tente novamente! ')