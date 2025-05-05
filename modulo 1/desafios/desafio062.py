primeiroTermo = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))

termos = primeiroTermo

contador = int(input('Quantos termos deseja mostrar? '))
contadorInicial = contador

while contador != 0:
    if contador == contadorInicial:
        print(primeiroTermo)
    else: 
        termos += razao
        print(termos)

    contador -= 1

    op = int(input('Deseja continuar a contagem? '))
    if op == 1:
        contador = int(input('Quantos termos deseja mostrar? '))
    termos += razao
    print(termos)

    contador -= 1
