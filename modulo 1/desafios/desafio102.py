def fatorial(n, show=False):
    """
        -> Calcula o fatorial de um numero
        :param n: O numero a ser calculado.
        :param show: (Opcional) Mostrar ou não a conta.
    """
    print('-' * 30)
    f = 1

    if show == True:
        for c in range(n, 0, -1):
            f *= c
            while c > 1:
                print(f'{c} X ', end="")
                break
            if c == 1:
                print(f'{c}', end="")
        print(f' = {f}')
    else:
        for c in range(n, 0, -1):
            f *= c
        print(f)
help(fatorial)
fatorial(5, False)