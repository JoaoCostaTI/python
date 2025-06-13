from uteis import numeros

num = int(input('Digite um valor: '))
fat = numeros.fatorial(num)
print(f'O Fatorial de {num} é {fat}')
print(f'O dobro de {num} é {numeros.dobro(num)}')
print(f'O Triplo de {num} é {numeros.triplo(num)}')