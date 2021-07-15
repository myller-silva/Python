lista = ('Lapis', 1.75,
         'Borracha', 2,
         'Caderno', 15.90,
         'Estejo', 25,
         'Transferidor', 4.20,
         'Compasso', 9.99,
         'Mochila', 120.32,
         'Canetas', 22.3,
         'Livros', 34.9)
print('-'*40)
print(f'{"LISTAGEM DE PREÇOS":^40}')
print('-'*40)
for posicao in range(0, len(lista)):
    if posicao % 2 == 0:
        print(f'{lista[posicao]:.<30}', end=' ')
    else:
        print(f'R$ {lista[posicao]:>6.2f}')
print('-'*40)