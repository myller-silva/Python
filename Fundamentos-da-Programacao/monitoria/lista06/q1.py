matriz = []

n = 2;
for i in range(0, n*n):
  matriz.append(input("nome: "));

for i in range(0, n*n):
  if(i%n==0):
    print()
  print(f"{matriz[i]}", end=" ");
print()
