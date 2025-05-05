import random

n = random.randint(0,10)
numeroUsuario = int(input('Digite um numero: '))
nPalpites = 0

while numeroUsuario != n: 
    print('Numero incorreto! Tente novamente! ')
    numeroUsuario = int(input('Digite um numero: '))
    nPalpites += 1

print('FIM DO JOGO!')
print(f'Parabéns! Vocẽ acertou o numero!\nSeu Número: {numeroUsuario}\nNumero do computador: {n}\nNumero de tentativas: {nPalpites}')



