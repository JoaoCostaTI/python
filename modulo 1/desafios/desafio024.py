nomeCidade = input('Digite o nome da cidade: ')

analisandoNome = nomeCidade.upper().lstrip().split()

print(analisandoNome)

if analisandoNome[0] == 'SANTO':
    print(f'A cidade começa com Santo, e seu nome é: {nomeCidade}')
else:
    print(f'A cidade não começa com Santo, e seu nome é: {nomeCidade}')
