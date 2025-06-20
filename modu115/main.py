from interface import *
from arquivo import *

arq = 'cursoemvideo.txt'

if not arquivoExiste(arq):
    criarArquivo(arq)



while True:
    cabecalho('MENU PRINCIPAL')
    resposta = menu(['Ver Pessoas Cadastradas', 'Cadastrar Pessoas', 'Sair do Programa'])

    if resposta == 1:
        # Opção de listar o conteúdo do arquivo:
        lerArquivo(arq)

    elif resposta == 2:
        cabecalho('OPÇÃO 2')
    elif resposta == 3:
        cabecalho('Saindo do sistema... até logo!')
        break
    else:
        print('ERRO! Digite uma opção válida!')
        

 