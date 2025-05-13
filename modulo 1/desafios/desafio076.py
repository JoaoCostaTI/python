produto = ('Pão', 1, 'Frango', 3.50, 'Queijo', 9.98, 'Ovo', 33.90 )

line_length = 40

print(20*"--")
print('Listagem de Produtos'.center(line_length))
print(20*"--")

nome = 0
preco = 1

contador = 0

while True:
        
    if nome < len(produto) and preco < len(produto):
        print(f'{produto[nome]}**********R${produto[preco]:.2f}')

    #Percorrendo a lista
    nome = preco + 1
    preco += 2

    #Contador para ir até o final da lista
    contador += 1

    if contador == len(produto):
        break

print(20*"--")

