palavras = ('Feijao', 'Arroz', 'Batata', 'Cenoura', 'Pera', 'Aprender')
palavra = ""

vogais = "AEIOUaeiou"

for c in range(0, len(palavras)):
    #Separando a palavra em uma única string
    palavra = palavras[c]

    #Percorrendo a string e verificando se tem vogais:
    print(f'Na palavra {palavra.upper()}',end=" temos " )
    for letra in palavra:
        if letra in vogais:
            print(letra.lower(), end=" ")
    print(end="\n")
        
    

        

