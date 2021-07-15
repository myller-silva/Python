soma = 0
for num in range(1, 7):
    n1 = int(input('Digite um número: '))
    if n1 % 2 == 0:
        soma += n1
print('a soma é {}'.format(soma))