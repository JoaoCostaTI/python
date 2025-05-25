matriz = [[7,3,2],[6,4,9],[1,5,3]]
somaPares = 0
somaTerceiraColuna = 0
linha = 0
maiorValorSegundaLinha = 0

for c in matriz:
    contador = 0
    linha += 1 

    for l in c:
        print(f'[{l}] ', end="")

        #Somando os numeros pares:
        if l % 2 == 0:
            somaPares += l

        #Somando valores da terceira coluna
        if contador == 2:
            somaTerceiraColuna += l
        contador += 1

        #Verificando o maior valor da segunda linha
        if linha == 2:
            if l > maiorValorSegundaLinha:
                maiorValorSegundaLinha = l
    print()
        

print(f'A soma de todos os valores pares é: {somaPares}')
print(f'A soma dos valores da terceira coluna é: {somaTerceiraColuna}')
print(f'O maior valor segunda linha = {maiorValorSegundaLinha}')