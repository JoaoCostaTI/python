import moeda

p = float(input('Digite um preço: R$'))
print(f'A Metade de {moeda.moeda(p)} é {moeda.metade(p, True)}')
print(f'O Dobro de {moeda.moeda(p)} é {moeda.dobro(p, True)}')
print(f'Aumentando 10%, temos {moeda.aumentar(p, 10, True)}')
print(f'Diminuindo 13%, temos {moeda.diminuir(p, 13, True)}')