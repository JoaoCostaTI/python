cb = (
    "Palmeiras",
    "Flamengo",
    "Red Bull Bragantino",
    "Cruzeiro",
    "Fluminense",
    "Atlético-MG",
    "Bahia",
    "Botafogo",
    "Ceará",
    "Corinthians",
    "Chapecoense",
    "Mirassol",
    "Internacional",
    "Grêmio",
    "São Paulo",
    "Santos",
    "Vasco da Gama",
    "Vitória",
    "Sport",
    "Juventude"
)

#Mostrando 5 primeiros colocados
print('*****OS Cinco primeiros colocados são:***** ')
for pos, c in enumerate(cb[:5]):
   print(f'{pos+1}º {c}')

#Mostrando os 4 ultimos
print('*****Os 4 ultimos colocados são:***** ')
for c in cb[-4:]:
    print(c)

#Ordenando em ordem alfabetica:
print('*****Ordenando os nomes dos times: *****')
print(sorted(cb))

#EM que posição está a chapecoense?
print(f'A chapecoense está na posição: {cb.index('Chapecoense')+1}')
