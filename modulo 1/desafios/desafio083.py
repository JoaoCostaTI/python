abertura = '('
fechamento = ')'

saldo = 0

expressao = str(input('Digite sua expressão: '))

for c in expressao:
    if saldo < 0:
        break
    if c == abertura:
        saldo += 1
    if c == fechamento:
        saldo -= 1

if saldo == 0:
    print('Expressão válida! ')
else: print('Expressão inválida! ')