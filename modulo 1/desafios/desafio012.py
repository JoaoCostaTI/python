preco = float(input('Qual o preço do produto? '))
reajuste = (preco * 5) / 100
valorFinal = preco - reajuste

print(f'O produto custa: R${preco}\nCom 5% de desconto fica: R${valorFinal}')