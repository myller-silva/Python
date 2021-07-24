# Utilize uma estrutura de controle em um algoritmo que imprime a tabuada de 1 a 3.

for n in range(1, 4):
    print(f"\nTABUADA DO {n}")
    for c in range(1, 11):
        print(f"{c:2d} x {n} = {c*n}")
print()
