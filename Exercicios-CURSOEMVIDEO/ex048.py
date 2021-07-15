# somar todos os numeros impares multiplos de 3 entre 1 e 500
soma = 0
valores = 0
for c in range(3, 500):
    if c%2 == 1:
        if c%3 == 0:
            soma = soma + c
            valores = valores +1
print('a soma de todos os {} valores é: {}.'.format(valores, soma))
