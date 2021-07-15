lista = []
dicio = {}
somaidade = 0
mulheres = []
acimamedia = []
while True:
    dicio['nome'] = str(input('Nome: '))
    sexo = ' '
    while sexo not in "MF":
        sexo = str(input('Sexo[M/F]: ')).upper().strip()[0]
        if sexo in 'MF':
            dicio['sexo'] = sexo
            if sexo == 'F':
                mulheres.append(dicio['nome'])
    dicio['idade'] = int(input('Idade: '))
    somaidade += dicio['idade']
    lista.append(dicio.copy())  # faz uma cópia de um dicionário
    esc = ' '
    while esc not in "SN":
        esc = str(input('Quer continuar? [S/N]')).upper().strip()[0]
    if esc == 'N':
        break
mediaidade = somaidade/len(lista)
for c in range(0, len(lista)):  #
    if lista[c]['idade'] > mediaidade:
        acimamedia.append(lista[c])  #
print(lista)
print(f'Ao todo temos {len(lista)} pessoas cadrastadas')
print(f'Media de idade: {mediaidade:.2f}')
print(f'mulheres cadastradas: {mulheres}')
print(f'acima da media estao: {acimamedia}')
