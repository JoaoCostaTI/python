vCasa = float(input("Qual é o valor da casa? R$ "))
salario = float(input('Qual é seu salário? R$ '))
anosPagamento = int(input("Em quantos anos você irá pagar? "))

prestacao30 = (salario * 30) / 100

prestacao = vCasa / (anosPagamento * 12)

if prestacao <= prestacao30:
    print(f'Emprestimo APROVADO! ')
    print(f'Valor da Prestação: R${prestacao:.2f}')
else: 
    print(f'Emprestimo NEGADO! ')
    print(f'O valor da prestação é: R${prestacao:.2f}\nE não pode ultrapassar o limite de 30% do seu salário que é R${prestacao30:.2f} ') 