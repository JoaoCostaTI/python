vel = float(input('Digite a velocidade do carro: '))


if vel >= 80:
    vLimite = vel - 80
    vMulta = 7 * vLimite
    
    print(f'Você foi multado! \nSua velocidade foi {vel}KM/h\nE o valor da sua multa é: R${vMulta:.2f}')
else:
    print(f'Sua velocidade foi: {vel}! Pode passar!')