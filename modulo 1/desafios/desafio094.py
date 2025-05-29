pessoas = []
dadosPessoas = {}
listaMulheres = []
listaPessoasIdadeAcimaDaMedia = []

totalIdade = 0
while True:
    #entrada dos dados
    dadosPessoas['nome'] = str(input('Nome: '))
    dadosPessoas['sexo'] = str(input('Sexo: [M/F] ')).upper().strip()
    dadosPessoas['idade'] = int(input('Idade: '))

    #Somando idades 
    totalIdade += dadosPessoas['idade']

    #adicionar na lista
    pessoas.append(dadosPessoas.copy())

    op = str(input('Deseja continuar? [S/N]'))

    if op in 'nN':
        break
print('-=' * 30)
#RESPOSTA A)
print(f'Foram cadastradas {len(pessoas)} pessoas. ')

for i, v in enumerate(pessoas):
    for k, valor in v.items():
        #Adicionando mulheres em uma lista separada
        if valor == 'F':
            listaMulheres.append(v["nome"])
    
#Calculando Media das idades
mediaIdades = totalIdade / len(pessoas)

#RESPOSTA B)
print(f'A média de idade do grupo é: {mediaIdades:.1f} anos. ')

#RESPOSTA C)
print(f'As mulheres cadastradas são: ', end="")
for c in listaMulheres:
    print(c, end="...")
print()

#RESPOSTA D)
for i, v in enumerate(pessoas):
     if v["idade"] >= mediaIdades:
        listaPessoasIdadeAcimaDaMedia.append(v)

print('-=' * 30)
print('Lista das pessoas que estão com idade acima da média: ')

for indice, v in enumerate(listaPessoasIdadeAcimaDaMedia):
    for k, valor in v.items():
        print(f'{k} = {valor};', end=" ")   
    print()