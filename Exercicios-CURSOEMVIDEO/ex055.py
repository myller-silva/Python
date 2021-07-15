menor = 0
maior = 0
for i in range(1, 6):
    n1 = float(input('Peso da {} pessoa'.format(i)))
    if i == 1:
        maior = n1
        menor = n1
    else:
        if n1 > maior:
            maior = n1
        if n1 < menor:
            menor = n1
print('O menor peso foi {}Kg e o maior foi {}Kg'.format(menor, maior))
