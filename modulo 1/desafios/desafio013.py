salario = float(input('Informe seu salário: R$ '))
porcentagemReajuste = 15
reajuste = salario + ((salario * porcentagemReajuste) / 100)


print(f'Seu salário atual é: R${salario:.2f}\nCom reajuste de {porcentagemReajuste}%\nO seu novo salário será: R${reajuste:.2f}')
