def leiaInt(msg):
    while True:
        try: 
            n = input(msg)
            return int(n)
        except KeyboardInterrupt:
            print(f'\nUsuário preferiu não informar os dados.')
            return 0
        except ValueError:
            print(f'ERRO! Por favor, repita e digite um valor inteiro VÁLIDO!')
        
def leiaFloat(msg):
    while True:
        try:
            n = input(msg)
            return float(n)
        except KeyboardInterrupt:
            print(f'\nUsuário preferiu não digitar esse numero')
            return 0
        except ValueError:
            print(f'ERRO! Por favor, repita e digite um valor Real VÁLIDO! ')

inteiro = leiaInt('Digite um numero INTEIRO ')
real = leiaFloat('Digite um numero REAL ')

print(f'O valor inteiro digitado foi {inteiro} e o real foi: {real}')