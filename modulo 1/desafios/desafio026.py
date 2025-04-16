frase = input('Digite uma frase: ').lower()
fraseFinal = frase.lstrip()

print(f'A letra A aparece {frase.count("a")}x')
print(f'A primeira ocorrencia é na posição: [{fraseFinal.find("a") + 1}]')
print(f'A Ultima ocorrencia é na posição: [{fraseFinal.rfind("a") + 1}]')