def leiaDado(msg):
    while True:
        entrada = str(input(msg)).strip().replace(',','.')

        if entrada.isalpha() or entrada == "":
            print(f'ERRO!!! {entrada} não é um valor válido, digite apenas numeros!')
        else:
            return float(entrada)

p = leiaDado('Digite um preço: R$')

print(f'{p} Preço ok!')