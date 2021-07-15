lista = []
while True:
    n = int(input('digite um valor: '))
    if n not in lista:
        lista.append(n)
    resp = ' '
    while resp not in 'SN':
        resp = str(input('quer continuar?[S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
lista.sort(reverse=True)
print(f'voce digitou os valores {lista}')
if 5 in lista:
    print(f'O valor 5 foi encontrado na posiçao {lista.index(5)}')
else:
    print('O valor 5 nao foi encontrado.')
print(f'voce digitou {len(lista)} valores')