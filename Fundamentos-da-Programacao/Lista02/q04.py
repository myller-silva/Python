# Crie um algoritmo que leia 3 números e imprima o maior valor

n1 = float(input("Digite o 1º numero: "))
n2 = float(input("Digite o 2º numero: "))
n3 = float(input("Digite o 3º numero: "))

if n1>n2 and n1>n3:
    maior = n1
elif n2>n1 and n2>n3:
    maior = n2
elif n3>n1 and n3>n2:
    maior = n3
else:
    maior = False

print(f"maior: {maior}")
