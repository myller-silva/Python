n1 = int(input('Primeiro termo: '))
r = int(input('Razao: '))
c = 0
esc = 10
while c != esc:
    print(n1, end='->' if c < (esc-1) else '. ')
    n1 += r
    c += 1
    if c == esc:
        esc = int(input('Quantos termos mais voce quer ver? '))
        if esc != 0:
            c = 0
        else:
            c = esc
print('FIM.')
