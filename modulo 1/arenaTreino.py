dados = {
    'nome' : 'Pedro',
    'idade' : 20,
    'Peso' : 74.8
}

pessoas = []

#Mostrar elemento especifico
print(dados['idade'])
print(dados['nome'])

#Adicionar um indice chamado Sexo inserindo M
dados['sexo'] = 'M'

#Remover elementos (Perde o indice e o valor)
del dados['idade']

#Diferenciação de elementos
dados.values() #Aqui retorna todos os VALORES dentro da lista
dados.keys() #Aqui retorna todas as chaves (Pensa nos índices de listas e tuplas)
print(dados.items()) #Retorna tudo, valores e keys

#Iterando os dados
for k, v in dados.items():
    print(f'O {k} é {v}')





