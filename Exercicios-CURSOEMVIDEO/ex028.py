#Jogo da Adivinhação v.1.0
from random import randint #randit randomiza um numero inteiro
computador = randint(0, 5)
msg = "Vou pensar em um numero entre 0 e 5. Tente adivinhar..."
lenMsg = len(msg)
qtd = (lenMsg//2)
barraX = '-=' * qtd +'-'*(lenMsg%2)
print(barraX)
print(msg)
print(barraX)
jogador = int(input('Em qual numero pensei? ')) # jogador tenta adivinhar
if jogador == computador:
    print('Parabens!!! Você me venceu!')
else:
    print('GANHEI! Eu pensei {} e não em {}!'.format(computador, jogador))
