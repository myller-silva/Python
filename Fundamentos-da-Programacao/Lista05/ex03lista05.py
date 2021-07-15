l = []
p = r = 0
for c in range(1, 11):
    n1 = int(input(f'Digite o {c} valor'))
    s = 0
    for r in range(1, n1 + 1):
        if n1 % r == 0:
            s += 1
    if s == 2:
        l += [r]
        p += 1
print(f'Os primos são: {l}. São {len(l)} números primos')
