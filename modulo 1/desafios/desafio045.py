import random

jogador = int(input('Escolha uma opção \n[1] Pedra\n[2] Papel\n[3] Tesoura\n'))

maquina = ['pedra', 'papel', 'tesoura']
escolhaMaquina = random.choice(maquina)

if jogador == 1 and escolhaMaquina == 'tesoura':
    print(f'Sua escolha: {jogador} Pedra\nEscolha da máquina: {escolhaMaquina} \nVOCE venceu!')
elif jogador == 2 and escolhaMaquina == 'pedra':
    print(f'Sua escolha: {jogador} Papel\nEscolha da máquina: {escolhaMaquina} \nVOCE venceu!')
elif jogador == 3 and escolhaMaquina == 'papel':
    print(f'Sua escolha: {jogador} Tesoura\nEscolha da máquina: {escolhaMaquina} \nVOCE venceu!')
elif escolhaMaquina == 'pedra' and jogador == 3:
    print(f'Sua escolha: {jogador} Tesoura\nEscolha da máquina: {escolhaMaquina} \nMÁQUINA venceu!') 
elif escolhaMaquina == 'papel' and jogador == 1:
    print(f'Sua escolha: {jogador} Pedra\nEscolha da máquina: {escolhaMaquina} \nMÁQUINA venceu!') 
elif escolhaMaquina == 'tesoura' and jogador == 2:
    print(f'Sua escolha: {jogador} Papel\nEscolha da máquina: {escolhaMaquina} \nMÁQUINA venceu!') 
else: print(f'EMPATE \nEscolha da máquina: {escolhaMaquina}')

import random

# Mapeamento das escolhas
opcoes = ['pedra', 'papel', 'tesoura']

# Entrada do jogador
jogador = int(input('Escolha uma opção \n[1] Pedra\n[2] Papel\n[3] Tesoura\n'))

# Validar entrada
if jogador not in [1, 2, 3]:
    print("Escolha inválida! Tente novamente com 1, 2 ou 3.")
else:
    escolha_jogador = opcoes[jogador - 1]
    escolha_maquina = random.choice(opcoes)

    print(f'Sua escolha: {escolha_jogador.capitalize()}')
    print(f'Escolha da máquina: {escolha_maquina.capitalize()}')

    # Verificando o resultado
    if escolha_jogador == escolha_maquina:
        print("EMPATE!")
    elif (escolha_jogador == 'pedra' and escolha_maquina == 'tesoura') or \
         (escolha_jogador == 'papel' and escolha_maquina == 'pedra') or \
         (escolha_jogador == 'tesoura' and escolha_maquina == 'papel'):
        print("VOCÊ venceu!")
    else:
        print("MÁQUINA venceu!")
