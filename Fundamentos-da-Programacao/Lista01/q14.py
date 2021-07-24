# Faça um algoritmo que calcule e imprima o An de uma P.A. (Progressão Aritmética), segundo a fórmula: An =
# a1 + (n-1) * r.

a1 = float(input('primeiro termo: '))
r = float(input('razao: '))
n = int(input('numero de termos: '))

an = a1+(n-1)*r

print(f"{n}º termo: {an}\n")
