from time import sleep

def contadorUm():
    print('=-' * 30)
    print('Contagem de 1 até 10 de 1 em 1: ')
    for c in range(1, 11):
        print(c, end=" ", flush=True)
        sleep(0.5)
    print('FIM!')
    

def contadorDois():
    print('=-' * 30)
    print('Contagem de 10 até 0 de 2 em 2: ')
    for c in range(10,-1,-2):
        print(c, end=" ", flush=True)
        sleep(0.5)
    print('FIM!')

def contador(inicio, fim, passo):
    print('=-' * 30)
    if inicio > fim:
        if passo <= 0:
            passo = 1
        if passo > 0:
            passo = -passo
            for c in range(inicio, fim - 1, passo):
                print(c, end=" ", flush=True)
                sleep(0.5)
            print('FIM! ')
            
        else:
            for c in range(inicio, fim - 1, passo):
                print(c, end=" ", flush=True)
                sleep(0.5)
            print('FIM! ')
    else:
        for c in range(inicio, fim, passo):
          print(c, end=" ", flush=True)
          sleep(0.5)
        print('FIM! ')

contadorUm()
contadorDois()
print('Agora é sua vez de personalizar a contagem: ')
contador(
    int(input('Inicio: ')),
    int(input('FIM: ')),
    int(input('Passo: '))
)
