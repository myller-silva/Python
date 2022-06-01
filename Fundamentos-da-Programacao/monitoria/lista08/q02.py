def saque(valor):
  cedulas = [2, 5, 10, 20, 50, 100, 200]
  cedulas.reverse()
  notas = []
  for cedula in cedulas:
    while(cedula <= valor):
      valor -= cedula
      notas.append(cedula)
  return notas


notas = saque(int(input("Digite o valor a ser sacado: ")))
print("Menor quantidade de notas: ", end="")
for nota in notas:
  print(nota, end=" ")
