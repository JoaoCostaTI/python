import interface 

while True:
    interface.cabecalho('MENU PRINCIPAL')
    resposta = interface.menu(['Ver Pessoas Cadastradas', 'Cadastrar Pessoas', 'Sair do Programa'])

    if resposta == 1:
        interface.cabecalho('Opção 1')
    elif resposta == 2:
        interface.cabecalho('OPÇÃO 2')
    elif resposta == 3:
        interface.cabecalho('Saindo do sistema... até logo!')
        break
    else:
        print('ERRO! Digite uma opção válida!')
        

 