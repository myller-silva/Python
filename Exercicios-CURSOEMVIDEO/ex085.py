lista = [[], []]
for c in range(1, 8):
    n = int(input(f'digite o {c}º número: '))
    if n % 2 == 0 and n not in lista[0]:
        lista[0].append(n)
    elif n % 2 == 1 and n not in lista[1]:
        lista[1].append(n)
lista[0].sort()
lista[1].sort()
print(f'números pares: {lista[0]}')
print(f'números impares: {lista[1]}')
