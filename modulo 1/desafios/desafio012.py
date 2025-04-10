preco = float(input('Qual o preço do produto? R$'))
reajuste = preco - ((preco * 5) / 100)


print(f'O produto custa: R${preco:.2f}\nCom 5% de desconto fica: R${reajuste:.2f}')