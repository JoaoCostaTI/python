lista = []

for c in range(5):
    #Pedindo os numeros
    n = int(input('Digite um valor: '))

    if c == 0:
        lista.append(n)

    for i in range(len(lista)):
        

print(f'Lista completa: {lista}')
