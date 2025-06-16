import moeda.formatacao
import moeda.moeda

p = float(input('Digite o preço: R$'))
print(f'A metade de {moeda.formatacao.real(p)} é {moeda.formatacao.real(moeda.moeda.metade(p))}')
print(f'O dobro de {moeda.formatacao.real(p)} é {moeda.formatacao.real(moeda.moeda.dobro(p))}')
print(f'Aumentando 10% temos {moeda.formatacao.real(moeda.moeda.aumentar(p, 10))}')