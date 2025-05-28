estado = dict()
brasil = list()

for c in range(3):
    nome = str(input('Digite o nome do estado: '))
    estado['uf'] = nome

    sigla = str(input('Digite a sigla: '))
    estado['sigla'] = sigla

    brasil.append(estado.copy())

for e in brasil:
    for valor in e.values():
        print(f'{valor}')