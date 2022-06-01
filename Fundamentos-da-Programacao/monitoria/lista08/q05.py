import random

def printMatrizResultado(nomes, voltas, format="02d"):
  print("nome \tvoltas\t\t\t\ttotal")
  for i in range(0, len(voltas)):
    print(f"{nomes[i]}:\t", end="")
    for j in range(0, len(voltas[i])):
      print(f"{voltas[i][j]:{format}} ", end="")
    print(f"  {sum(voltas[i])}", end="")
    print()


def melhorVolta(matriz, nomes):
  corredorComMelhorVolta = nomes[0]
  menor = matriz[0][0]
  i=0
  for corredor in matriz:
    for volta in corredor:
      if(volta<menor):
        menor = volta
        corredorComMelhorVolta = nomes[i]
    i+=1
  
  print(f"melhor volta: {menor}")
  print(f"corredor: {corredorComMelhorVolta}")
  return menor


def lerDados():
  nomes = []
  matriz = []
  for i in range(0, 6):
    nomes.append(random.randint(3,52)) # nomes.append(input(f"Nome do {i+1} corredor: "))
    voltas = []
    for j in range(0, 10):
      voltas.append(random.randint(3,52)) # voltas.append(input(f"Tempo na {j+1} volta: "))
    matriz.append(voltas)
    # print()
  return [nomes, matriz]





dados = lerDados()
nomes = dados[0]
matriz = dados[1]

printMatrizResultado(nomes, matriz)
print()
melhorVolta(matriz, nomes)
