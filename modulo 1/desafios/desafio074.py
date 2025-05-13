from random import randint

contador = 0

tupla = ()

maior = 0
menor = 51

#Gerando os numeros 5 vezes
while True:
    elemento = randint(0,10)
    tupla += (elemento,)

    contador += 1
    if contador == 5:
        break

    #Verificando o maior elemento: 
    if elemento > maior:
        maior = elemento
    if elemento < menor:
        menor = elemento

#Mostrando os 5 numeros gerados: 
print("Os elementos da tupla são: ")
print(tupla)

print(f'Maior elemento: {maior}')
print(f'Menor elemento: {menor}')

