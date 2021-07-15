#Aumentos múltiplos
sal = float(input('O salário é: R$ '))
if sal <= 1250:
    novo = sal * 1.15
else:
    novo = sal * 1.1
print('Quem ganhava R${:.2f} passa a ganhar R${:.2f}.'.format(sal, novo))
