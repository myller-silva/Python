#039 - Alistamento Militar
from datetime import date
anoatual = date.today().year   # ano atual
nasc = int(input('Ano de nascimento: '))
idade = anoatual - nasc
print('Quem nasceu em {} completa {} anos em {}.'.format(nasc, idade, anoatual))
if idade == 18:
    print('Deve se alistar imediatamente.')
elif idade < 18:
    ano = (18 - idade)
    print('Voce ainda nao tem 18 anos. Seu ano de alistamento será em {}.'.format(anoatual + ano))
elif idade > 18:
    ano = (idade - 18)
    print('Você deveria ter se alistado em {}. Procure a junta militar mais proxima.'.format(anoatual - ano))
