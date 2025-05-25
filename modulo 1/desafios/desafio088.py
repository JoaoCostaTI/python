from random import randint
from time import sleep

palpites = []
palpitesFinais = []

jogos = int(input('Quantos palpites de jogos gerar? '))

for qtdJogos in range(jogos):
    #Preenchendo os 6 numeros
    contador = 0
    for jogo in range(2):
        numeroMega = randint(1,60)
        if contador == 0:
            palpites.append(numeroMega)
            contador += 1
        else:
            while len(palpites) < 6:
                numeroMega = randint(1,60)
                if numeroMega not in palpites:
                    palpites.append(numeroMega)

    #Adicionando os palpites na lista final
    palpitesFinais.insert(qtdJogos, palpites[:])

    #Limpando lista palpites
    palpites.clear()

#ordenando as listas
for sublista in palpitesFinais:
    sublista.sort()

#Exibindo os resultados
linhaJogo = 1
for linha in palpitesFinais:
    sleep(0.5)
    print(f'Jogo {linhaJogo}: {linha}')
    linhaJogo += 1