n = 0

while True:
    n = int(input('Tabuada de qual numero? '))

    if n < 0:
        break

    for c in range(11):
        print(f'{n} x {c} = {n*c}')

print('Fim')