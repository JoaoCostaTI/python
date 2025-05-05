# 1. Ler quantos termos mostrar
quantidade = int(input('Quantos termos você quer mostrar? '))

# 2. Inicializar os dois primeiros termos
anterior = 0
atual = 1

# 3. Contador para controlar os termos mostrados
contador = 0

# 4. Loop para exibir a sequência
while contador < quantidade:
    # → Aqui você imprime o termo atual
    
    print(anterior)

    # → Aqui você calcula o próximo termo (anterior + atual)
    proximoTermo = anterior + atual

    # → Atualiza os valores:
    anterior = atual
    #    - anterior vira atual
    atual = proximoTermo
    #    - atual vira próximo

    # → Incrementa o contador
    contador += 1