palavras = ('aprender', 'programar', 'linguagem', 'python', 'curso', 'gratis', 'estudar', 'praticar', 'trabalhar', 'mercado', 'programador', 'futuro')

vogais = 'aeiou'

palavra = ""

#Percorrendo cada palavra
for c in range(0, len(palavras)):
    
    #Atribuindo cada palavra da tupla a uma string separada
    palavra = palavras[c]

    print(f'\nNa palavra {palavra.upper()} temos:', end=" ")
    
    #Percorrendo para capturar apenas as vogais
    for i in palavra:
        if i in vogais:
            print(i, end=" ")
    

