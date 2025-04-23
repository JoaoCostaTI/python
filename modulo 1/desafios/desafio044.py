preco = float(input('Digite o valor do produto: R$: '))
fPagamento = int(input("Qual será a forma de pagamento?\n[1] A VISTA (10% de desconto)\n[2] A VISTA CARTÃO (5% de desconto)\n[3] ATÉ 2x CARTÃO (Preço Normal)\n[4] 3x OU MAIS NO CARTÃO (20% de Juros) "))

if fPagamento == 1:
    preco10 = (preco * 10) / 100 
    preco10Final = preco - preco10
    print(f'Valor do Produto R${preco:.2f} com desconto de 10% R${preco10Final:.2f} ')
elif fPagamento == 2: 
    preco5 = (preco * 5) / 100 
    preco10Final = preco - preco5
    print(f'Valor do Produto R${preco:.2f} com desconto de 5% R${preco10Final:.2f} ')
elif fPagamento == 3:
    preco = preco / 2
    print(f'O Valor do produto R${preco:.2f} dividido de 2x, serão 2 parcelas de R${preco:.2f}')
else: 
    preco30 = (preco * 20) / 100
    preco30Final = preco30 + preco
    
    nParcelas = int(input('Quantas parcelas deseja dividir? '))

    if nParcelas >= 3 and nParcelas <= 10:
        precoParcelado = preco30Final / nParcelas
        print(f'Sua compra será parcelada de {nParcelas}x de R${precoParcelado:.2f} COM JUROS!\nSua compra de R${preco:.2f} vai custar R${preco30Final:.2f} ')

    
print('Fim')