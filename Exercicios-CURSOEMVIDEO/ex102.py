def fatorial(num, show=False):
    """
    => Calcula o fatorial de um número
    :param num: O numero a ser calculado
    :param show: (opcional) Mostrar ou não a conta
    :return: o valor do Fatorial de num
    """
    fat = 1
    print(f"{num}! =", end=' ')
    if show:
        for c in range(num, 0, -1):
            print(f"{c}", 'x' if c != 1 else '=', end=' ')
    while num > 0:
        fat *= num
        num -= 1
    return fat


# PROGRAMA PRINCIPAL
print(fatorial(5, True))
#help(fatorial)
