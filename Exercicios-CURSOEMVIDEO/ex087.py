lista = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
par = somacoluna3 = maiorlinha2 = 0
for linha in range(0, 3):
    for coluna in range(0, 3):
        lista[linha][coluna] = int(input(f'Posição [{linha}, {coluna}]: '))
        if lista[linha][coluna] % 2 == 0:
            par += lista[linha][coluna]
        if coluna == 2:
            somacoluna3 += lista[linha][coluna]
        if linha == 1 and coluna == 0 or linha == 1 and lista[linha][coluna] > maiorlinha2:
            maiorlinha2 = lista[linha][coluna]
for linha in range(0, 3):
    for coluna in range(0, 3):
        print(f'[{lista[linha][coluna]:^5}]', end=' ')
    print()
print(f'A soma dos valores pares foi: {par}')
print(f'A soma da terceira coluna foi: {somacoluna3}')
print(f'O maior valor da segunda linha foi: {maiorlinha2}')
