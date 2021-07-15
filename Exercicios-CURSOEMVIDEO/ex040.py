n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
media = (n1 + n2)/2
if 7 > media >= 0:
    print('Sua media foi {}. Voce está reprovado.'.format(media))
elif 7 <= media <= 10:
    print('Sua nota foi {}. Você foi aprovado.'.format(media))
else:
    print('A media {} é invalida. Tente novamente.'.format(media))
