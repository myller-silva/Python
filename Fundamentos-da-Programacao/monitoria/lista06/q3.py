from math import pow; from random import randint

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
  if(somatorio(matriz, 0, n*n, n)!=chave): return False
  for i in range(1, n):
    if(somatorio(matriz, i*n, i*n+n, 1) != chave): return False   #linhas
    if(somatorio(matriz, i-1, n*n, n) != chave): return False     #colunas
  if(somatorio(matriz, 0, n*n, n+1) != chave): return False       #diagonal principal
  if(somatorio(matriz, n-1, n*n-1, n-1) != chave): return False   #diagonal secundaria
  return True

# exemplos de quadrados magicos: [4, 9, 2, 3, 5, 7, 8, 1, 6], [5, 5, 5, 5, 5, 5, 5, 5, 5], [6, 1, 8, 7, 5, 3, 2, 9, 4], [8, 1, 6, 3, 5, 7, 4, 9, 2], [2, 7, 6, 9, 5, 1, 4, 3, 8], [8, 0, 7, 4, 5, 6, 3, 10, 2]
matriz = [] ; n = 2
for i in range (0, n*n): matriz.append(randint(0, 9))
if(n*n!=len(matriz) or n==1):	
  print("quantidade insuficiente de elementos\n")
  exit()
printMatriz(matriz, n, "3d")
str = "É" if(ehQuadradoMagico(matriz, n)) else "NÃO é"
print(f"\n{str} uma matriz QUADRADO MÁGICO ")
