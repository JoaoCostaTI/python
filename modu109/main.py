from ex109 import moeda

p = float(input('Digite um preço: R$'))

print(f'A metade de {moeda.moeda(p)} é: {moeda.metade(p, True)}')
print(f'O dobro de {moeda.moeda(p)} é: {moeda.dobro(p, True)}')
print(f'Aumentando em 10% temos {moeda.aumentar(p, 10, True)}')
print(f'Diminuindo 13% {moeda.diminuir(p, 13, True)}')