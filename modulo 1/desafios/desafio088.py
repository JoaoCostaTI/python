from random import randint
from time import sleep

palpites = []
palpitesFinais = []

jogos = int(input('Quantos palpites de jogos gerar? '))

for qtdJogos in range(jogos):
    #Preenchendo os 6 numeros
    for jogo in range(6):
        palpites.insert(qtdJogos, randint(1,60))

    #Adicionando os palpites na lista final
    palpitesFinais.insert(qtdJogos, palpites[:])

    #Limpando lista palpites
    palpites.clear()

#Exibindo os resultados
linhaJogo = 1
for linha in palpitesFinais:
    sleep(0.5)
    print(f'Jogo {linhaJogo}: {linha}')
    linhaJogo += 1
