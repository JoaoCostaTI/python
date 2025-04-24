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
