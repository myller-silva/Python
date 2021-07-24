# Faça um algoritmo que receba o raio R de uma esfera e calcule o seu volume: V = (4 * Pi * R3)/3.
from math import pow

pi = 3.14
r = int(input("Digite o raio da esfera(m): "))
v = ( 4.0 * pi * pow(r, 3) ) /3


print(f"volume: {v:.2f}m³")
