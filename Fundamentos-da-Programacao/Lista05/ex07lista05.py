from random import sample
n1 = sample(range(1, 20), 10)
n2 = int(input('Digite um numero: '))
if n2 in n1:
    i = n1.index(n2)
    print(f'O numero {n2} está na posição {i} do vetor')
else:
    print(f'O numero {n2} não está no vetor')
