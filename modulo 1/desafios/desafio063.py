print('*Sequencia de Fibonacci*')

n = int(input('Quantos termos? '))

t1 = 0
t2 = 1

print(t1, end=" => ")
print(t2, end=" => ")

contador = 3

while contador <= n:
    t3 = t2 + t1

    print(t3, end=" => ")

    contador += 1

    t1 = t2
    t2 = t3

print(' FIM')