lista = []
n = str(input('digite sua expressão: '))
for simbolo in n:
    if simbolo == '(':
        lista.append('(')
    if len(lista) != 0:
        if simbolo == ')':
            lista.pop()
if len(lista) == 0:
    print(n)
    print(lista)
    print('Sua expressão é valida!')
else:
    print(n)
    print(lista)
    print('sua expressão não é valida!')
