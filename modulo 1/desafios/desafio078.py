numeros = []

maior = 0
menor = 999999999

listaIndiceMaior = []
listaIndiceMenor = []


for c in range(0,5):
    #Inserindo os valores na lista
    n = int(input(f'Digite o numero da posição {c}º: '))
    numeros.append(n)

    listaMaior = numeros[:]
    listaMenor = numeros[:]

for i, v in enumerate(numeros):
    print(f'Indice: {i}, Número: {v}' )

    #Verificando qual o maior valor:
    if v >= maior:
        maior = v
        
        listaMaior.sort(reverse=True)
        if maior == listaMaior[0]:
            listaIndiceMaior.append(i)
    
    #verificando qual o menor valor: 
    if v <= menor:
        menor = v
        
        listaMenor.sort()
        if menor == listaMenor[0]:
            listaIndiceMenor.append(i)
  
print(f'Os valores digitados foram: {numeros}')

print(f'O maior valor digitado foi: {maior} na posição: {listaIndiceMaior}')
print(f'O menor valor digitado foi: {menor} na posição: {listaIndiceMenor}')
