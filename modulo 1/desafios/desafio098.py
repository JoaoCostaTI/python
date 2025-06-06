from time import sleep

def contador(inicio, fim, passo):
    if passo < 0:
        passo *= -1
    if passo == 0:
        passo = 1
    print(f'Contagem de {inicio} até {fim} de {passo} em {passo}')
    
    if inicio < fim:
        for c in range(inicio, fim+1, passo):
            print(f'{c}', end=" ", flush=True)
            sleep(0.5)
        print('FIM!')
    else:
        for c in range(inicio, fim-1, -passo):
            print(f'{c}', end=" ", flush=True)
            sleep(0.5)
        print('FIM!')

contador(1,10,1)
contador(10,0,2)
print('Agora é sua ver de personalizar a contagem! ')
inicio = int(input('Inicio: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
contador(inicio, fim, passo)