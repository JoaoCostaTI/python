cedula50 = 0
cedula20 = 0
cedula10 = 0
cedula1 = 0



while True:
    print(20*'=')
    print('    BANCO JCOSTA     ')
    print(20*'=')
    valorSaque = int(input('Que valor você deseja sacar? R$'))

    #Calculando quantidade de cedulas de 50:
    if valorSaque >= 50:
        cedula50 = valorSaque // 50 #Aqui pega o valor da divisão INTEIRA
        valorSaque -= (cedula50 * 50)
    
    #Calculando quantidade de cedulas de 20:
    if valorSaque >= 20:
        cedula20 = valorSaque // 20 #Aqui pega o valor da divisão INTEIRA
        valorSaque -= (cedula20 * 20)
    
    #Calculando quantidade de cedulas de 10:
    if valorSaque >= 10:
        cedula10 = valorSaque // 10 #Aqui pega o valor da divisão INTEIRA
        valorSaque -= (cedula10 * 10)
    
    #Calculando quantidade de cedulas de 1:
    if valorSaque >= 1:
        cedula1 = valorSaque // 1 #Aqui pega o valor da divisão INTEIRA
        valorSaque -= (cedula1 * 1)

    break

print(f'Total de {cedula50} cédulas de R$50,00')
print(f'Total de {cedula20} cédulas de R$20,00')
print(f'Total de {cedula10} cédulas de R$10,00')
print(f'Total de {cedula1} cédulas de R$1,00')


