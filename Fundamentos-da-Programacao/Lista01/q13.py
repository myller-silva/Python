# Fazer um algoritmo para ler dois números inteiros e trocar seus valores; (ex.: A e B; valor de A passa para o B
# e valor de B passa para o A); e depois imprimir os novos valores de cada variável.

a = int(input('Digite o valor de A: '))
b = int(input('Diite o valor de B: '))
temp = a
a = b
b = temp

print(f"\nA: {a}\nB: {b}\n")
