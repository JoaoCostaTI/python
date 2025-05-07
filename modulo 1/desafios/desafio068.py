from random import randint

print("=-"*13)
print('VAMOS JOGAR PAR OU ÍMPAR!')
print("=-"*13)

vitoriasJogador = 0


while True:
    #Numero do computador:
    computador = randint(0,11)
    
    #NUmero do Jogador
    jogador = int(input('Digite um valor: '))
    #Selecionar se irá ser Par ou Impar
    opcao = str(input('Par ou Impar? [P/I]')).upper().strip()

    resultado = computador + jogador

    print(f'Você jogou {jogador} e o computador {computador}')
    print(f'Total deu: {resultado}')

    #Condição onde o jogador escolhe par:
    if opcao == 'P':
        if resultado % 2 == 0:
            print('Você GANHOU! ', end=" ")
            vitoriasJogador += 1
            print(f'Você venceu: {vitoriasJogador} vezes')
        else:
            print('Você perdeu! ')
            print(f'Você venceu: {vitoriasJogador} vezes')
            break
    #Condição jogador escolhe Impar: 
    if opcao == 'I':
        if resultado % 2 == 1:
            print('VOCê GANHOU!', end=" ")
            vitoriasJogador += 1
            print(f'Você venceu: {vitoriasJogador} vezes')
        else:
            print('Você perdeu! ')
            print(f'Você venceu: {vitoriasJogador} vezes')
            break