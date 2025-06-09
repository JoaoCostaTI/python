def par(n=0):
    if n%2 == 0:
        return True
    else:
        return False

numero = int(input("Digite um numero: "))

retorno = par(numero)

if retorno == True:
    print(f'{numero} é PAR!')
else:
    print(f'{numero} é IMPAR')