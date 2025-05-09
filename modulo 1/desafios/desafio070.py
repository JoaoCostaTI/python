totalCompra = 0
produtos1000Mais = 0
nomeProdutoMaisBarato = ''
precoProdutoMaisBarato = 0
cont = 0

while True:
    print('*******Cadastro de Produtos******')
    nomeProduto = str(input('Digite o nome do produto: '))
    precoProduto = float(input('Digite o preço do produto: R$'))
    continuar = str(input('Continuar o cadastro? [S/N]')).strip().upper()

    #Calculando o gasto total da compra:
    totalCompra += precoProduto

    #Calculando produtos que custam mais de R$1000
    if precoProduto >= 1000:
        produtos1000Mais += 1
    

    #Descobrindo nome do produto mais barato:
    if cont == 0:
        precoProdutoMaisBarato = precoProduto
        cont += 1
    if precoProduto < precoProdutoMaisBarato:
        precoProdutoMaisBarato = precoProduto
        nomeProdutoMaisBarato = nomeProduto
    
    #Saindo do programa:
    if continuar == 'N':
        break

print(f'O total gasto foi: R${totalCompra:.2f}')
print(f'Um total de {produtos1000Mais} custaram mais de R$1000')
print(f'O nome do produto mais barato é: {nomeProdutoMaisBarato} e custou R${precoProdutoMaisBarato:.2f}')

