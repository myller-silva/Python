# Faça um algoritmo para calcular e imprimir o An de uma P.G. (Progressão Geométrica)
from math import pow

a1 = float(input("Primeiro termo: "))
q = float(input("Razao: "))
n = int(input("Numero de termos: "))

an = a1*pow(q, n-1)

print(f"{n}º termo: {an}\n")
