'''
frase = input('Digite uma frase: ')
fraseNormal = frase.replace(" ", "").lower()
fraseInvertida = fraseNormal[::-1]

if fraseNormal == fraseInvertida:
    print(f'A frase [{frase}] é um Palindromo')

'''

frase = input('Digite uma frase: ').strip().upper()
junto = frase.replace(" ", '')

inverso = ""

for c in range (len(junto) - 1, -1, -1):
    inverso += junto[c]

print(f'Analisando as palavras [Frase] = {junto}\n[Inverso] = {inverso}')

print('-' * 20)
if inverso == junto:
    print(f'{junto} e {inverso} são Palindromo! ')
else: print(f'{junto} e {inverso} não são Palindromo! ')
