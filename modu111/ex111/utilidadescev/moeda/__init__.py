def aumentar(preco=0, taxa=0, formato=False):
    res = preco + (preco*taxa/100)
    if formato is False:
        return res 
    else: 
        return moeda(res)

def diminuir(preco=0, taxa=0, formato=False):
    res = preco - (preco*taxa/100)
    if formato is False:
        return res
    else: 
       return moeda(res)

def dobro(preco=0, formato = False):
    res = preco * 2
    return res if formato is False else moeda(res)

def metade(preco=0, formato = False):
    res = preco / 2
    return res if formato is False else moeda(res)


#Formata os preços
def moeda(preco=0, moeda= 'R$'):
    return f'{moeda}{preco:>.2f}'.replace('.',',')

def resumo(preco=0, vA=10, vD=5):
    tam = 35
    print('-'*tam)
    print(f'{"RESUMO DO VALOR".center(tam)}')
    print('-'*tam)

    print(f'Preço analisado: \t{moeda(preco)}')
    print(f'Dobro do preço: \t{dobro(preco, True)}')
    print(f'Metade do preço: \t{metade(preco, True)}')
    print(f'{vA}% de aumento: \t{aumentar(preco, vA, True)}')
    print(f'{vD}% de redução: \t{diminuir(preco, vD, True)}')
