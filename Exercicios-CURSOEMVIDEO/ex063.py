n = int(input('Quantos termos da sequencia de fibonacci voce quer mostrar? '))
t1 = 0
t2 = 1
c = 2
if n > 2:
    print('{}, {}, '.format(t1, t2), end='')
    while c != n:
        tx = t1 + t2
        t1 = t2
        t2 = tx
        c += 1
        print('{}'.format(tx), end=', ' if c != n else '.')
