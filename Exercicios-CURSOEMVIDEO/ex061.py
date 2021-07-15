n1 = int(input('Primeiro termo da PA: '))
r = int(input('Razao da PA: '))
c = 0
while c != 10:
    print(n1, end='')
    print(', 'if c < 9 else '.', end='')
    n1 += r
    c += 1
