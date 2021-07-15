v = [1, 2, 3, 4, 5]
n1 = int(input('Digite um número'))
if n1 in v:
    index = v.index(n1)
    print(f'O numero {n1} está na posição {index}')
else:
    print(f'O numero {n1} não está no vetor')
