import random


def printMatriz(matriz):
  for corredor in matriz:
    c = corredor
    print(corredor)
  return



matriz = {}

for i in range(0, 6):
  nome = i
  voltas = []
  for j in range(0, 10):
    volta = random.randint(50, 100)
    voltas.append(volta)
  matriz[nome] = voltas
  
teste = {"myller":[123, 23], "mac":[123, 321]}
# print(matriz)
printMatriz(matriz)

# print(teste)