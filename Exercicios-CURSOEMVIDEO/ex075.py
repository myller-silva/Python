par = 0
lista = (int(input('digite um numero: ')), int(input('digite um numero: ')), int(input('digite um numero: ')), int(input('digite um numero: ')))
print(lista)
print(f'O valor 9 apareceu {lista.count(9)} vezes.')
if 3 in lista:
    print(f'O valor 3 apareceu na {lista.index(3)+1}ª posição.')
else:
    print('O valor 3 não foi digitado')
print('os valores pares foram: ')
for c in lista:
    if c % 2 == 0:
        par += 1
        print(f'"{c}"', end=' ')
print(f'A quantidade de numeros pares foi {par}.')
