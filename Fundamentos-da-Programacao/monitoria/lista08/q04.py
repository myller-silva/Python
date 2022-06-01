def linhaDeMaiorSoma(matriz, n):
  linha = matriz[0:n:1] # primeira linha
  maior = sum(linha) 
  for i in range (n, n*n, n):
    aux = matriz[i:i+n]
    temp = sum(aux)
    if(temp>maior):
      maior = temp
      linha = aux
  return linha


def printMatriz(matriz=0, lin=0, col=0, format = "3d"):
  for i in range(0, lin*col):
    if(i%lin==0):
      print()
    print(f"{matriz[i]:{format}}", end=" ")
  print()



# matriz = [
#   1, 2, 4,
#   2, 4, 6,
#   0, 12, 5
# ]
matriz = []
for i in range(0, 3*3, 1):
  matriz.append(int(input(f"Digite o {i+1} elemento: ")))

printMatriz(matriz, 3)

print(f"Linha de maior soma: {linhaDeMaiorSoma(matriz, 3)}")
print(f"Soma: {sum(linhaDeMaiorSoma(matriz, 3))}")
