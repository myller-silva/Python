contidade = cmen = women20 = 0
while True:
    idade = int(input('Idade: '))
    if idade > 18:
        contidade += 1
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo[M/F]: ')).strip().upper()[0]
    if sexo == 'M':
        cmen += 1
    if sexo == 'F' and idade < 20:
        women20 += 1
    esc = ' '
    while esc not in 'SN':
        esc = str(input('Quer continuar?[S/N] ')).strip().upper()[0]
    if esc == 'N':
        break
print(f'Total de pessoas com mais de 18 anos: {contidade}')
print(f'Homens cadastrados: {cmen}')
print(f'Mulheres com menos de 20 anos cadastradas: {women20}')
