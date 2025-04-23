from datetime import datetime

try:
    ano_nascimento = int(input('Qual seu ano de nascimento? '))
    ano_atual = datetime.now().year
    idade_atual = ano_atual - ano_nascimento

    if idade_atual < 18:
        tempo_restante = 18 - idade_atual
        print(f'Sua idade é {idade_atual} anos. Ainda faltam {tempo_restante} anos para o alistamento.')
    elif idade_atual == 18:
        print(f'Sua idade é {idade_atual} anos. Você deve se alistar AGORA!')
    else:
        tempo_excedente = idade_atual - 18
        print(f'Sua idade é {idade_atual} anos. Já passaram {tempo_excedente} anos do prazo para alistamento.')
except ValueError:
    print("Erro: Por favor, digite um número válido para o ano de nascimento.")