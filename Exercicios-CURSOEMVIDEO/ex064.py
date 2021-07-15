n1 = 0
soma = 0
while n1 != 999:
    n1 = int(input('Digite um numero [999 para parar]:'))
    if n1 != 999:
        soma += n1
print('A soma dos valores foi {}.'.format(soma))
