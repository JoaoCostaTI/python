

def leiaDinheiro(num):
    n = num
    while True:
        n = input(num).strip().replace(',', '.')
        if n.replace('.','', 1).isdigit():
            nFormatado = float(n)
            break
        else:
            print('Digite um valor válido! ')
    return nFormatado