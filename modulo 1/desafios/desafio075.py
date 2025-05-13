numeros = ()
numerosPares = ()

contador = 0

while True:
    #Lendo os numeros
    n = int(input('Digite um numero: '))

    #Armazenando na tupla
    numeros += (n, )

    #Verificando os numeros pares
    if n % 2 == 0:
        numerosPares += (n, )

    #Controle para ler apenas 4 numeros
    contador += 1

    if contador == 4:
        break

    
#Quantidade de vezes que aparece o valor 9
print(f'O numero 9 aparece: {numeros.count(9)}x')

#Posição que foi digitado o numero 3
if 3 in numeros:
    print(f'O numero 3 foi digitado a primeira vez na posição: {numeros.index(3)+1}')
else:
    print(f'O Numero 3 não foi digitado nenhuma vez')

#Numeros pares de dentro da Tupla
print(f'Os numeros pares foram: {numerosPares}')

