from random import sample
n1 = sample(range(1, 100), 10)
n2 = []
par = impar = 0
for c in n1:
    if c % 2 == 0:
        par +=1
    else:
        impar += 1
print(f'Há {par} numeros pares e {impar} impares no vetor')
