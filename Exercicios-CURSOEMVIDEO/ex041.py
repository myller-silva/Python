#Classificando Atletas
from datetime import date
ano = date.today().year
nasc = int(input('Ano de nascimento do atleta: '))
idade = ano - nasc
if idade <= 9:
    print('Mirim')
elif idade <= 14:
    print('Infantil')
elif idade <= 19:
    print('Junior')
elif idade <= 25:
    print('Sênior')
else:
    print('Master')
