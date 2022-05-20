from math import pow

def printMatriz(matriz, n, format):
  for i in range(0, n*n):
    if(i%n==0): print()
    print(f"{matriz[i]:{format}}", end=(" "))


def somatorio(vetor, inicio, ate, passo):
  soma = 0
  for i in range(inicio, ate, passo): soma += vetor[i]
  return soma


def ehQuadradoMagico(matriz, n):
  chave = somatorio(matriz, 0, n, 1);
  for i in range(1, n):
    if(somatorio(matriz, i*n, i*n+n, 1) != chave): return False		#linhas
    if(somatorio(matriz, i-1, n*n, n) != chave): return False 		#colunas
  if(somatorio(matriz, 0, n*n, n+1) != chave): return False 		  #diagonal principal
  if(somatorio(matriz, n-1, n*n-1, n-1) != chave): return False   #diagonal secundaria
  return True


# exemplos: [4, 9, 2, 3, 5, 7, 8, 1, 6], [5, 5, 5, 5, 5, 5, 5, 5, 5], [6, 1, 8, 7, 5, 3, 2, 9, 4], [8, 1, 6, 3, 5, 7, 4, 9, 2], [2, 7, 6, 9, 5, 1, 4, 3, 8], [8, 0, 7, 4, 5, 6, 3, 10, 2]
matriz = [16, 3, 2, 13, 5, 10, 11, 8, 9, 6, 7, 12, 4, 15, 14, 1]
n = (int)(pow(len(matriz), 0.5))
if(n*n!=len(matriz)):
  print("quantidade insuficiente de elementos")
  exit()

printMatriz(matriz, n, "3d")
str = "É" if(ehQuadradoMagico(matriz, n)) else "NÃO é"
print(f"\n{str} uma matriz QUADRADO MÁGICO ")
