n1 = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
n2 = []
for c in n1:
    if c % 2 == 0:
        n2.append(c)
    n2.sort(reverse=True)
print(n2)
