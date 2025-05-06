n = int(input('Digite o numero para calcular fatorial: '))
fat = 1

'''
while n > 0:
    fat *= n
    n -= 1
print(fat)
'''

for c in range(n, 0, -1):
    fat = fat * n
    n -= 1
print(fat)
