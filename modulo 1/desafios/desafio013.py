salario = float(input('Informe seu salário: R$ '))
porcentagemReajuste = 15
reajuste = (salario * porcentagemReajuste) / 100
valorFinal = salario + reajuste

print(f'Seu salário atual é: R${salario}\nCom reajuste de {porcentagemReajuste}%\nO seu novo salário será: R${valorFinal}')