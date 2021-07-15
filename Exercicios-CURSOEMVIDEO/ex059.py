n = 0
p = 0
n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
while n != 5:
    print("""[1] SOMAR
[2] MULTIPLICAR
[3] MAIOR
[4] NOVOS NÚMEROS
[5] SAIR DO PROGRAMA""")
    n = int(input('Qual sua escolha? '))
    if n == 1:
        soma = n1 + n2
        print('{} + {} = {}.'.format(n1, n2, soma))
    elif n == 2:
        p = n1 * n2
        print('{} x {} = {}.'.format(n1, n2, p))
    elif n == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print('O maior entre {} e {} é {}.'.format(n1, n2, maior))
    elif n == 4:
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
    elif n > 5:
        print('Opçâo inválida. Tente novamente.')
