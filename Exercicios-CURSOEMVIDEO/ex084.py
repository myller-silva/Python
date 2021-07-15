lista = []
pesados = []
leves = []
esc = ' '
while True:
    temp = [str(input('nome: ')), float(input('peso[Kg]: '))]
    lista.append(temp[:])
    if lista[-1][1] >= 100:
        pesados.append(lista[-1])
    elif lista[-1][1] <= 70:
        leves.append(lista[-1])
    while esc not in 'SN':
        esc = str(input('quer continuar? [S/N] ').upper().strip()[0])
    if esc == 'N':
        break
    temp.clear()
    esc = ' '
print(f'Voce cadastrou {len(lista)} pessoa(s)')
print('Os mais pesados foram: ')
for c in range(0, len(pesados)):
    print(f'{pesados[c][0]} com {pesados[c][1]}Kg')
print('Os mais leves foram: ')
for c in range(0, len(leves)):
    print(f'{leves[c][0]} com {leves[c][1]}Kg')
