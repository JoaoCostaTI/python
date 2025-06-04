def maior(*num):
    print('=-' * 30)
    print(f'Analisando os valores passados...', end="")
    print()
    for c in num:
        print(f'{c}', end=" ")
    print(f'Foram informados {len(num)} ao todo. ')
    print(f'O maior numero é: {max(num)}')

maior(2,9,4,5,7,1)
maior(4,7,0)
maior(1,2)
maior(6)
maior(0)

