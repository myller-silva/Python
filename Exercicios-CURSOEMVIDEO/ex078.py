lista = list()
for pos in range(0, 5):
    lista.append(int(input('Digite um numero para a posição {}: '.format(pos))))
    if pos == 0:
        maior = menor = lista[pos]
    else:
        if lista[pos] > maior:
            maior = lista[pos]
        if lista[pos] < menor:
            menor = lista[pos]
print(f'\nO maior valor foi {maior} nas posições', end=' ')
for c, v in enumerate(lista):
    if v == max(lista):
        print(f'{c}', end='...')
print(f'\nO menor valor foi {menor} nas posições ', end='')
for c, v in enumerate(lista):
    if v == min(lista):
        print(f'{c}', end='...')
