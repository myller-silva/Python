# Progressao Aritmetica
print('='*25)
print('10 TERMOS DE UMA P.A.')
print('='*25)
n1 = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
for c in range(1, 11):
    print(n1, end=' ')
    n1 += razao
