#ler o preço de um produto e ler o novo preço com 0,05 de deconto
preco = float(input('Preço do protuto: '))
desc = 0.05
preco_desconto = preco*(1-desc)
print('O preço com 5% de desconto é {}'.format(preco_desconto))
