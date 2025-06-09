def fatorial(n, show=False):
    print('-' * 30)
    f = 1

    if show == True:
        for c in range(n, 0, -1):
            f *= c
            while c > 1:
                print(f'{c} X ', end="")
                continue
            if c == 1:
                print(f'{c}', end="")
        print(f' = {f}')
    else:
        for c in range(n, 0, -1):
            f *= c
        print(f)


fatorial(5, True)