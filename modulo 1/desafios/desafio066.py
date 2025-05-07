n = 0
qtdNumeros = 0
soma = 0

while True:
    n = int(input('Digite um numero: '))

    if n == 999:
        break

    qtdNumeros += 1
    soma += n
print(f'Foram digitados: {qtdNumeros} numeros\nSoma de todos: {soma}\n')