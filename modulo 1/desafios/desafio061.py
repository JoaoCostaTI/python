primeiroTermo = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))

termos = primeiroTermo

'''
for c in range(10):
    if c == 0:
        print(primeiroTermo)
    else: 
        termos += razao
        print(termos)
'''

contador = 10

while contador != 0:
    if contador == 10:
        print(primeiroTermo)
    else: 
        termos += razao
        print(termos)
        
    #Contador para girar 10x
    contador -= 1