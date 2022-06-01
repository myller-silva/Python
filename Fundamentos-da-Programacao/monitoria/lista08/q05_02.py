import random


def lerDados():
  matriz = {}
  for i in range(0, 6):
    nome = i
    voltas = []
    for j in range(0, 10):
      volta = random.randint(50, 100)
      voltas.append(volta)
    matriz[nome] = voltas
  return matriz

def printMatriz(matriz, format="3d"):
  chaves = list(matriz.keys())
  tam = len(matriz)
  for i in range(0, tam):
    print(chaves[i], end=": ")
    voltas = matriz[i]
    for volta in voltas:
      print(f"{volta:{format}}", end=" ")
    print()
  return


def melhorVolta(matriz):
  chaves = list(matriz.keys())
  menor = matriz[0][0]
  corredor = chaves[0]
  tam = len(matriz)
  for i in range(0, tam):
    voltas = matriz[i]
    for volta in voltas:
      if(volta<menor):
        menor=volta
        corredor = chaves[i]
  print(f"melhor volta: {menor}s, corredor: {corredor}")


def classificacao(matriz):
  # chaves = list(matriz.keys())
  # resultado = []
  # menor = sum(matriz[0])
  # tam = len(matriz)
  # for i in range(0, tam):
  #   temp = sum(matriz[i])
  #   if(temp<menor):
  #     menor = temp
  return





matriz = lerDados()
printMatriz(matriz)
print()
melhorVolta(matriz)
classificacao(matriz)


# print(teste.keys)