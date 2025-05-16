lista = []

for c in range(0, 5):
    #Solicitando os numeros
    n = int(input('Digite um valor: '))

    #Adicionando itens no final da lista, ou seja, o MAIOR
    #lista[-1] sempre irá validar o ultimo elemento
    if c == 0 or n > lista[-1]:
        lista.append(n)
        print('Adicionado ao final da lista...')
    else:
        pos = 0
        while pos < len(lista):
            if n <= lista[pos]:
                lista.insert(pos, n)
                print(f'Adicionado na posição {pos} da lista...')
                break
            pos += 1
print(lista)