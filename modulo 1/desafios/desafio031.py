distancia = float(input('Qual será a distancia da viagem? '))

if distancia <= 200:
    preco = distancia * 0.5
    print(f'A distancia da sua viagem sera: {distancia:.2f}KM\nE o custo da viagem será: R${preco:.2F}')
else:
    preco = distancia * 0.45
    print(f'A distancia da sua viagem sera: {distancia:.2f}KM\nE o custo da viagem será: R${preco:.2F}')