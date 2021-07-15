dias = int(input('Quantos dias? '))
km = float(input('Quantos quilometros rodados? '))
preco = dias*60 + km*0.15
print('O valor a ser pago por {} dias e {}km é R${}.'.format(dias, km, preco))
