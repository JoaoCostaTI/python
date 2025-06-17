def moeda (num):
    return f"R${num:.2f}"

def metade(num, f=False):
    if f:
        return f"R${num/2:.2f}"
    else:
        return num / 2

def dobro(num, f=False):
    if f:
        return f"R${num*2:.2f}"
    else:
        return num * 2

def aumentar(num, vA=10, f=False):
    if f:
        return f"R${num + ((num*vA/100)):.2f}"
    else:
        return num + ((num*vA)/100)

def diminuir(num, vD=13, f=False):
    if f:
        return f"R${num - ((num*vD/100)):.2f}"
    else: 
        return num - ((num*vD)/100)
def resumo(num, vA=80, vD=35):
    tam = 30
    print("-" * tam)
    print(f'{"RESUMO DO VALOR".center(tam)}')
    print("-" * tam)

    print(f'{"Preço analisado:":<15}{moeda(num):>15}')
    print(f'{"Dobro do preço:":<15}{dobro(num, True):>15}')
    print(f'{"Metade do preço:":<15}{metade(num, True):>15}')
    print(f'{f"{vA}% de Aumento:":<15}{aumentar(num, vA, True):>15}')
    print(f'{f"{vD}% de Redução:":<15}{diminuir(num, vD, True):>15}')
