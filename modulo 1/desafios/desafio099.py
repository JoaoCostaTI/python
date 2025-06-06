def maior(*num):
    print('=-' * 30)
    print(f'Analisando os valores passados...')
    c = maior = 0
    for valor in num:
        print(f"{valor}", end=" ")
        if c == 0:
            maior = valor
        if valor > maior:
            maior = valor
        c += 1
    print(f'Foram informados {len(num)} valores ao todo...')
    print(f'O maior valor foi: {maior}')
maior(2,9,4,5,7,1)
maior(4,7,0)
maior(1,2)
maior(6)
maior()

