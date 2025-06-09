def notas(*listaNotas, sti=False):
    dicionarioNotas = {}

    total = 0
    media = 0
    for c in listaNotas:
        if total == 0:
            dicionarioNotas['maior'] = dicionarioNotas['menor'] = c
        else:
            if c > dicionarioNotas['maior']:
                dicionarioNotas['maior'] = c
            if c < dicionarioNotas['menor']:
                dicionarioNotas['menor'] = c
        media += c
        total += 1

    dicionarioNotas['media'] = round(media / total, 1)
    dicionarioNotas['total'] =  total

    if sti == True:
        if dicionarioNotas['media'] >= 7:
            dicionarioNotas['situacao'] = 'BOA'
        elif dicionarioNotas['media'] > 6:
            dicionarioNotas['situacao'] = 'RAZOÁVEL'
        else:
            dicionarioNotas['situacao'] = 'RUIM'   

    return dicionarioNotas

resp = notas(3.5, 6.5, 2, 7, 4, sti=True)

print(resp)