primeiroTermo = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))

termos = primeiroTermo


for c in range(10):
    if c == 0:
        print(primeiroTermo)
    else: 
        termos += razao
        print(termos)

