n = [0, 0, 0]
for c in range(0, 3):
    n[c] = int(input(f"Digite o {c+1} valor: "))

print()
print(n)
me = sum(n) / len(n)
print(me)
