import random

n = random.randint(0,10)
numeroUsuario = int(input('Digite um numero: '))
nPalpites = 1

while numeroUsuario != n: 
    if n < numeroUsuario:
        print('MENOS!... Numero incorreto! Tente novamente! ')
        numeroUsuario = int(input('Digite um numero: '))
        nPalpites += 1
    else:
        print('MAIS!... Numero incorreto! Tente novamente! ')
        numeroUsuario = int(input('Digite um numero: '))
        nPalpites += 1

print('FIM DO JOGO!')
print(f'Parabéns! Vocẽ acertou o numero!\nSeu Número: {numeroUsuario}\nNumero do computador: {n}\nNumero de tentativas: {nPalpites}')



