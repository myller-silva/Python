esc = 'S'
media = cont = maior = menor = 0
while esc != 'N':
    n1 = int(input('Digite um numero: '))
    media += n1
    cont += 1
    if cont == 1:
        menor = maior = n1
    elif n1 > maior:
        maior = n1
    elif n1 < menor:
        menor = n1
    esc = str(input('Quer continuar [S/N]:')).strip().upper()[0]
    if esc not in 'SsNn':
        esc = str(input('Escolha inválida. Quer continuar [S/N]: ')).strip().upper()[0]
media = media/cont
print('Voce digitou {} numeros, a media foi {:.2f}. Maior: {}. Menor {}.'.format(cont, media, maior, menor))
