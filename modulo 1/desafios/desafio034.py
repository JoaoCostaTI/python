salario = float(input('Digite seu salário: '))
aumento10 = 10
aumento15 = 15
reajuste = 0

if salario >= 1250:
    print('Reajuste de 10%')
    reajuste = (salario * aumento10) / 100
    salarioF = reajuste + salario
    print(f'Seu salário é: R${salario:.2f}\nCom o reajuste de {aumento10}% = R${reajuste:.2f} seu novo salário será: R${salarioF:.2f}')
else:
    print('Reajuste de 15%')
    reajuste = (salario * aumento15) / 100
    salarioF = reajuste + salario
    print(f'Seu salário é: R${salario:.2f}\nCom o reajuste de {aumento15}% = R${reajuste:.2f} seu novo salário será: R${salarioF:.2f}')
