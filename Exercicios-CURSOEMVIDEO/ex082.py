lista = []
par = list()
impar = list()
while True:
    n = int(input('Digite um numero: '))
    if n not in lista:
        lista.append(n)
        if n % 2 == 0:
            par.append(n)
        else:
            impar.append(n)
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar?[S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print(f'A lista completa é: {lista} \nLista de pares: {par} \nA lista de impares: {impar}')
