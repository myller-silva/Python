def printMatrizResultado(nomes, voltasMatriz, format="02d"):
  print("nome \tvoltas")
  for i in range(0, len(voltasMatriz)):
    print(f"{nomes[i]}:\t", end="")
    for j in range(0, len(voltasMatriz[i])):
      print(f"{voltasMatriz[i][j]:{format}} ", end="")
    print()


def lerDados():
  nomes = []
  matriz = []
  for i in range(0, 6):
    nomes.append(i) # nomes.append(input(f"Nome do {i+1} corredor: "))
    voltas = []
    for j in range(0, 10):
      voltas.append(i*j) # voltas.append(input(f"Tempo na {j+1} volta: "))
    matriz.append(voltas)
    # print()
  return [nomes, matriz]




dados = lerDados()
nomes = dados[0]
matriz = dados[1]



printMatrizResultado(nomes, matriz)
