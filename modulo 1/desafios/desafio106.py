def ajuda(com):
     help(com)

def titulo(msg, cor=0):
    tam = len(msg) + 4 
    print('~' * tam)
    print(msg.center(tam))
    print('~' * tam)

comando = ''

while True:
    titulo('SISTEMA DE AJUDA PyHELP')
    comando = str(input('Função ou Biblioteca >: '))
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)

titulo('ATÉ LOGO')