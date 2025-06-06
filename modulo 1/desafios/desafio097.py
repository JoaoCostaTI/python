def escreva(msg):
    linhas = len(msg) + 4
    print('~' * linhas)
    print(msg.center(linhas))
    print('~' * linhas)
escreva(str(input('Qual mensagem escrever? ')))