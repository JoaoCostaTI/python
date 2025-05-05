qtdNumeros = 0

parar = 999
somaNumeros = 0

while parar == 999:
    #Digitar valores
    n = int(input('Digite um valor: '))

    #atualizar Contador
    qtdNumeros += 1

    #Somar numeros:
    somaNumeros += n

    #Condição de parada
    if n == 999:
        qtdNumeros -= 1
        somaNumeros -= 999
        break
print(f'Foram digitados {qtdNumeros} numeros\nA soma de todos é: {somaNumeros}')