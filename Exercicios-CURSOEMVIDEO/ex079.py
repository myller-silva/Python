lista = list()
while True:
    lista.append(int(input('Digite um valor: ')))
    if lista[-1] in lista[:-1]:
        lista.pop()
        print('valor duplicado. nao vou adicionar.')
    esc = ' '
    while esc not in 'SN':
        esc = input('Quer continuar?[S/N] ').upper().strip()[0]
    if esc == 'S':
        print('CONTINUAR')
    if esc == 'N':
        print('PARAR')
        break
print(lista)
