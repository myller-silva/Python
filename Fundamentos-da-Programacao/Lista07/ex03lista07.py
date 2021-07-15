def maior(q, w, r, e):
    a = int(q)
    b = int(w)
    c = int(r)
    ma = int(e)
    if a > b and a > c:
        ma = a
    if b > a and b > c:
        ma = b
    if c > a and c > b:
        ma = c
    return ma
a = int(input('Primeiro valor: '))
b = int(input('Segundo valor: '))
c = int(input('Terceiro valor: '))
ma = 0
print('O maior valor entre os tres digitados é: ', maior(a, b, c, ma))
