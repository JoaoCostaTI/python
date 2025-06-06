def escopo():
    print("Controle de Terrenos".center(30))
    print('-' * 30)

def area (width, lenght):
    area = width * lenght
    print(f'A área de um terreno {width}x{lenght} é de {area:.1f}m²')

escopo()

area(
    float(input('LARGURA (m): ')), 
    float(input('COMPRIMENTO (m): '))
)