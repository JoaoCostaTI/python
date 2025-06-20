# Aqui ele tenta executar o programa
try:
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a/b
# Caso der errado vem para aqui 
except (ValueError, TypeError):
    print('Tivemos um problema com os tipos de dados que vc digitou. ')
except ZeroDivisionError:
    print('Não é possivel dividir um numero por zero!')
except KeyboardInterrupt:
    print('Usuário preferiu não informar os dados. ')
except Exception as erro:
    print(f'O erro encontrado foi: {erro.__cause__}')
else: 
    # Caso der certo vem para aqui   
    print(f'O resultado é {r:.1f}')
    print('Deu Certo!')
finally:
    # Aqui vai ser executado sempre, se der certo ou não.  
    print('Volte sempre Muito obrigado! ')
