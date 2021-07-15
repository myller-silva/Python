# Maior e menor valores
n1 = float(input('primeiro valor: '))
n2 = float(input('segundo valor: '))
n3 = float(input('terceiro valor: '))
menor = n1
# verificando menor
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3
# verificando maior
maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n2 and n3 > n1:
    maior = n3
print('Entre os numeros digitados, o menor foi {:.2f} e o maior foi {:.2f}'.format(menor, maior))