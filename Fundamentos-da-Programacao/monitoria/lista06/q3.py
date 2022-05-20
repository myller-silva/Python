from math import pow

def printMatriz(matriz, n, format):
  for i in range(0, n*n):
    if(i%n==0 and i!=0): print()
    print(f"{matriz[i]:{format}}", end=(" "))


def somatorio(vetor, inicio, ate, passo):
  soma = 0
  for i in range(inicio, ate, passo):
    soma += vetor[i]
  return soma


def ehQuadradoMagico(matriz, n):
  linhas = []; colunas = []; chave = 0
  # linhas:
  for i in range(0, n):
    linhas.append( somatorio(matriz, i*n, i*n+n, 1) )
    if(i==0): chave = linhas[0];continue
    if(linhas[i]!=chave): return False
  # colunas:
  for i in range(0, n):
    colunas.append( somatorio(matriz, inicio=i, ate=n*n, passo=n) )
    if(colunas[i]!=chave ): return False
  # diagonais:
  diagonalPrincipal = somatorio( matriz, inicio=0, ate=n*n, passo=n+1 )
  if(diagonalPrincipal!=chave): return False
  diagonalSecundaria = somatorio( matriz, inicio=n-1, ate=n*n-1, passo=n-1 )
  if(diagonalSecundaria!=chave): return False
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
