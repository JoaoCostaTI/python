primeiroTermo = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))
termo = primeiroTermo
cont = 1
total = 0
mais = 10


while mais != 0:
    total += mais
    while cont <= total:
        print(termo)
        termo += razao
        cont += 1
    print('Pausa')

    mais = int(input('Quantos termos você quer mostrar? '))
print('FIM')
