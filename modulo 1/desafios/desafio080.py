lista = []

for c in range (5):
    n = int(input('Digite um numero: '))

    if c == 0 or n > lista[-1]:
        lista.append(n)
        print('Adicionado no final da lista...')
    else:
        controle = 0
        while controle < len(lista):
            if n <= lista[controle]:
                lista.insert(controle, n)
                print(f'Adicionado na posição {controle}')
                break
            controle += 1

print(f'Lista completa ordenada: {lista}')