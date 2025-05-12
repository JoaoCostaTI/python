contagem = ("zero", "um", "dois", "três", "quatro", "cinco", "seis", "sete", "oito", "nove", "dez", "onze", "doze", "treze", "quatorze", "quinze", "dezesseis", "dezessete", "dezoito", "dezenove", "vinte")

n = int(input('Digite um numero ENTRE 0 E 20: '))

while True:
    if n < 0 or n > 20:
        n = int(input('TENTE NOVAMENTE! Digite um numero ENTRE 0 E 20: '))
    if n >= 0 and n <= 20:
        break

print(f'Número digitado foi: {n} = {contagem[n]}')
