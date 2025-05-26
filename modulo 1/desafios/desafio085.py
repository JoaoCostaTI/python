valores = [[],[]]

for c in range(7):
    n = int(input('Digite um valor: '))

    if n % 2 == 0:
        valores[0].append(n)
    else:
        valores[1].append(n)

valores[0].sort()
valores[1].sort()

for lista in range(len(valores)):
    if lista == 0:
        print(f'Lista PARES = {valores[lista]}')
    else:
        print(f'Lista IMPARES = {valores[lista]}')
