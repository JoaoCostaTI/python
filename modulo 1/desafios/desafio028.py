import random
from time import sleep

n = random.randint(0,5)

nUser = int(input('Digite um numero entre [0] e [5]: '))

print('--------INICIO DO GAME-------')

print('Processando...')
sleep(2)
if nUser == n:
    print(f'Numero do computador: {n}\nSeu numero: {nUser}\nParabéns! Você acertou!')
else:
    print(f'Numero do computador: {n}\nSeu numero: {nUser}\nTente novamente! Você errou!')
print('--------FIM DO GAME-------')