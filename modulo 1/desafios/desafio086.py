matriz = [[],[],[]]

for c in range(3):
    for i in range(3):
        n = int(input(f'Digite o valor da posição {c,i}: '))
        matriz[c].insert(i, n)
    

for coluna in matriz:
    for linha in coluna:
        print(f'[ {linha} ] ', end="")
    print()