from math import pow; from random import randint

def printMatriz(matriz, n, format):
  for i in range(0, n*n):
    print(f"{matriz[i]:{format}}", end='\n' if((i+1)%n==0) else '')

def ehQuadradoMagico(matriz, n):
  chave = sum(matriz[0 : n*n : n+1]) #diagonal principal
  if(sum(matriz[n-1 : n*n-1 : n-1])!=chave): return False #diagonal secundaria
  for i in range(0, n):
    if(sum(matriz[i*n : i*n+n : 1]) != chave): return False #linhas
    if(sum(matriz[i : n*n : n] ) != chave): return False #colunas
  return True

matriz = [] ; n = 3   #exemplo de quadrado magico: [4, 9, 2, 3, 5, 7, 8, 1, 6]
for i in range (0, n*n): matriz.append(randint(0, 9))
if(n*n!=len(matriz) or n==1):	
  exit("quantidade insuficiente de elementos")
printMatriz(matriz, n, "3d")
print(f"\n{'É' if(ehQuadradoMagico(matriz, n)) else 'NÃO é'} uma matriz QUADRADO MÁGICO.")
