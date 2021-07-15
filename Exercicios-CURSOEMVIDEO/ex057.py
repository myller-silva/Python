n = ''
while n != 'M' and n != 'F':
    n1 = str(input('SEXO: ')).strip().upper()[0]
    if n1 in 'MF':
        n = n1
    else:
        print('valor inválido.')
