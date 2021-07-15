#Jogo da Adivinhação v.1.0
from random import randint  #randit randomiza um numero inteiro
pc = randint(0, 10)
print('Sou seu computador. Acabei de pensar num numero.')
jogador = int(input('Qual seu palpite? '))
tentativas = 1
while jogador != pc:
    if pc > jogador:
        print('Mais... Tente de novo')
    else:
        print('Menos... Tente de novo.')
    jogador = int(input('Outro palpite: '))
    tentativas += 1
print('Jogador = {} e PC = {}. Precisou de {} tentativas'.format(jogador, pc, tentativas))
