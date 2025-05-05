c = 's'

media = 0
qtdMedia = 0

maior = 0
menor = 9999999


while c != 'n':
    n = float(input('Digite um numero: '))

     #Somando os numeros para posteriormente calcular a média
    media += n
    qtdMedia += 1

    #Descobrindo quem é o maior:
    if n < menor:
        menor = n
    if n > maior:
        maior = n

    continuar = str(input('Deseja continuar? ')).lower() 
    if continuar == 'n':
        c = continuar  

mediaFinal = media / qtdMedia

print(f'Você digitou {qtdMedia} numeros e A média dos numeros digitados foi: {mediaFinal:.2f}')
print(f'MAIOR = {maior}\nMENOR = {menor}')