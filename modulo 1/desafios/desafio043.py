peso = float(input('Digite o seu peso: '))
altura = float(input('Digite sua altura: '))

imc = peso / altura ** 2 

if imc < 18.5:
    print(f'ABAIXO DO PESO!\nSeu IMC é: {imc:.1f}')
elif imc > 18.4 and imc < 26:
    print(f'PESO IDEAL!\nSeu IMC é: {imc:.1f}')
elif imc > 25 and imc < 31:
    print(f'SOBREPESO!\nSeu IMC é: {imc:.1f}') 
else: print(f'OBESIDADE MORBIDA!\nSeu IMC é: {imc:.1f}')