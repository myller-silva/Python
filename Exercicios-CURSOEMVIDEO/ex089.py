lista = [[], [[], []], []]    #aluno \ notas \ medias
while True:
    aluno = str(input('Nome do aluno: ')).upper()
    lista[0].append(aluno)
    soma = 0
    for c in range(0, 2):
        n = float(input(f'nota {c+1}: '))
        lista[1][c].append(n)
        soma += n
    lista[2].append(soma/2)
    esc = ' '
    while esc not in 'SN':
        esc = str(input('quer continuar?[S/N] ')).upper().strip()[0]
    if esc == 'N':
        break
print(f'{"Nº":<3}{"ALUNO":<10}{"MÉDIA":>20}')
for c in range(0, len(lista[0])):
    print(f'{c:<3}{lista[0][c]:<10}{lista[2][c]:>20}')
while True:
    ver = ' '
    if (ver not in lista[0]) or (ver != 'F'):
        ver = str(input('quer ver as notas de qual aluno? [F para interromper]')).upper()
    if ver in lista[0]:
        print('nota 1 = ', lista[1][0][lista[0].index(ver)], '\nnota 2 = ', lista[1][1][lista[0].index(ver)])
    if ver == 'F':
        break

