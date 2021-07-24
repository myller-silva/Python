# Crie um algoritmo para ler 3 valores float e imprimir o quadrado do 1º + a soma dos outros dois.

n = []
for c in range (0, 3):
    n.append(float(input(f"Digite o {c+1}º valor: ")))

print( f"\n{n[0]}² = {n[0]**2}" )
print( f"{n[1]} + {n[2]} = {n[1]+n[2]}\n" )
