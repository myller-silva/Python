from datetime import date
anoatual = date.today().year
maiores = 0
menores = 0
for i in range(1, 8):
    n1 = int(input('Ano de nascimento da {}ª pessoa: '.format(i)))
    idade = anoatual - n1
    if idade < 18:
        menores = menores + 1
    else:
        maiores = maiores + 1
print('Há {} menores de idade e {} maiores de idade.'.format(menores, maiores))
