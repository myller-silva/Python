n1 = [2**2, 4**2, 6**2, 8**2, 10**2, 12**2, 14**2, 16**2, 18**2, 20**2]
n2 = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
n3 = 0
n4 = 0
for notan1 in n1:
    n3 += notan1
for notan2 in n2:
    n4 += notan2
print(f'A soma ds vetores é: {n3+n4}')
