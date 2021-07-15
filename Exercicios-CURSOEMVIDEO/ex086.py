lista = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for linha in range(0, 3):
    for coluna in range(0, 3):
        lista[linha][coluna] = int(input(f'Posição [{linha}, {coluna}]: '))
for linha in range(0, 3):
    for coluna in range(0, 3):
        print(f'[{lista[linha][coluna]:^5}]', end=' ')
    print()
