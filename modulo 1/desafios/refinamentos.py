numero = input('Digite algo: ')

if numero.isnumeric():
    numero = int(numero)
    print('Sim é um numero!!!')
if isinstance(numero, str):
    print('Sim é string!!!')