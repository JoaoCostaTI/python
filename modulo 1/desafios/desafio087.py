matriz = [[0,0,0],[0,0,0],[0,0,0]]

for linha in range(3):
    for coluna in range(3):
        matriz[linha][coluna] = int(input(f'Digite um valor para {linha, coluna}'))


somaPares = 0
somaTerceiraColuna = 0
maiorValorSegundaLinha = None

for linha in range(3):
    for coluna in range(3):
        #Exibindo os resultados 
        print(f'[ {matriz[linha][coluna]:^5} ]', end=" ")
    

        #Somando Pares
        if matriz[linha][coluna] % 2 == 0:
            somaPares += matriz[linha][coluna]

        #Somando apenas terceira coluna
        if coluna == 2:
            somaTerceiraColuna += matriz[linha][coluna]
        
        #Verificando qual maior valor da segunda linha
        if linha == 1:
            if matriz[linha][coluna] > maiorValorSegundaLinha:
                maiorValorSegundaLinha = matriz[linha][coluna]
    print()

print(f'A soma dos valores pares é: {somaPares}')
print(f'A Soma da terceira coluna é: {somaTerceiraColuna}')
print(f'O maior valor da segunda linha e: {maiorValorSegundaLinha}')