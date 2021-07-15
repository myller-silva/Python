dia = int(input('digite o dia: '))
mes = int(input('digite o mes: '))
ano = int(input('digite o ano: '))
l = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro',
     'novembro', 'dezembro']
valida = False
if mes == 0 or mes == 2 or mes == 4 or mes == 6 or mes == 8 or mes == 10 or mes == 12:
    if dia <= 31:
        valida = True
elif mes == 3 or mes == 5 or mes == 7 or mes == 9 or mes == 11:
    if dia <= 30:
        valida = True
elif mes == 2:
    if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
        if dia <= 29:
            valida = True
        elif dia <= 28:
            valida = True
if valida:
    print('Data valida')
    print(f'{dia} de {l[mes - 1]} de {ano}')
else:
    print('Data invalida')
