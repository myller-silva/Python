n1 = int(input('Digite um numero para saber seu fatorial: '))
fat = 1
while n1 != 1:
    fat = fat * n1
    n1 -= 1
print('o fatorial é {}'.format(fat))
