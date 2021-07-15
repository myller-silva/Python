#Analisando Triângulo v1.0
n1 = float(input('Primeiro segmento: '))
n2 = float(input('Segundo segmento: '))
n3 = float(input('Terceiro segmento: '))
if n1 < (n2 + n3) and n2 < (n1 + n3) and n3 < (n1 + n2):
    print('{:.2f}, {:.2f} e {:.2f} PODEM FORMAR um triângulo.'.format(n1, n2, n3))
else:
    print('{:.2f}, {:.2f} e {:.2f} NÃO PODEM FORMAR um triângulo.'.format(n1, n2, n3))
