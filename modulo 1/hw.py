from math import sqrt,pow,ceil,floor

def calcular(num1, num2, operacion):
  resultado = 0

  if operacion == '+':
    resultado = num1 + num2
    return print(f'{resultado}') 
  
  elif operacion == '-':
    resultado = num1 - num2
    return print(f'{resultado}') 
   
  elif operacion == '*':
    resultado = num1 * num2
    return print(f'{resultado}')  
  
  elif operacion == '/':

    if num2 == 0:
      return "Error: No se puede dividir por cero."
    resultado = num1 / num2

    return print(f'{resultado}') 
   
  else:
    return "Error: Operación no válida."
  
calcular(
  int(input('Digite um numero: ')), int(input('Digite outro numero: ')), input('Qual o tipo de operação? ')
)

