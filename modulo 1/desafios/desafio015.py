diasAlugados = int(input('Quantos dias alugados? '))
kmRodado = float(input('Quantos Km Rodados? '))

dia = 60
km = 0.15

valorAPagar = diasAlugados * dia + kmRodado * km

print(f'O total a pagar é: R${valorAPagar:.2f}')