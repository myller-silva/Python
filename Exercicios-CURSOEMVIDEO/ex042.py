# Analisando Triângulos v2.0
n1 = float(input('Primeiro segmento: '))
n2 = float(input('Segundo segmento: '))
n3 = float(input('Terceiro segmento: '))
if n1 <(n2 + n3) and n2 < (n1 + n3) and n3 < (n1 + n2):
    if n1 == n2 == n3:
        print('Triângulo equilátero')
    elif n1 == n2 or n1 == n3 or n2 == n3:
        print('Triangulo isóceles')
    else:
        print('Triangulo escaleno')
else:
    print('{:.1f}, {:.1f} e {:.1f} nao podem formar triangulo'.format(n1, n2, n3))
