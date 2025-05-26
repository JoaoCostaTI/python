dados = []
listaFinal = []

while True:
    nome = str(input('Nome: '))
    dados.append(nome)
    
    for nota in range(2):
        notas = float(input(f'Nota {nota+1}: '))
        dados.append(notas)

    listaFinal = dados[:]

    dados.clear()

    op = str(input('Deseja continuar? [S/N]: ')).upper().strip()

    if op in 'nN':
        break

print(listaFinal)