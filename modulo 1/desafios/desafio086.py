matriz = []

for linha in range(3):
    linha_temporaria = []
    for coluna in range(3):
        n = int(input(f'Digite um valor para [{linha}, {coluna}]: '))
        linha_temporaria.append(n)
    matriz.append(linha_temporaria)


for indiceLinha, linha in enumerate(matriz):
    for indiceColuna, coluna in enumerate(matriz):
        print(f' [{matriz[indiceLinha][indiceColuna]}] ', end="")
    print()