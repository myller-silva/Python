cont = totCompra = produto1000 = barato = 0
while True:
    produto = str(input('Produto: '))
    preco = float(input('Preço: R$'))
    cont += 1
    if cont == 1 or preco < barato:
        barato = preco
        nomebarato = produto
    if preco > 1000:
        produto1000 += 1
    totCompra += preco
    esc = ' '
    while esc not in 'SN':
        esc = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    if esc == 'N':
        break
print(f'{totCompra:.2f}')
print(f'{produto1000}')
print(f'{barato:.2f}')
print(f'{nomebarato}')
