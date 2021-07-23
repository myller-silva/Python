from os import system

system("cls")

n = float(input("Valor unitario: "))
qt = int(input("Quantidade: "))

print(f"preço total a pagar: R${ n*qt :.2f}\n\n")