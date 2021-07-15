n1 = int(input('Digite um numero: '))
total = 0
for c in range(1, n1+1):
    if (n1 % c == 0):
        total += 1
if total != 2:
    print('O numero {} não é primo'.format(n1))
else:
    print('O numero {} é primo'.format(n1))