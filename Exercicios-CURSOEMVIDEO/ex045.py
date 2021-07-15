# PEDRA, PAPEL, TESOURA
from random import randint
itens = ( 'Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print('''Suas opções:
[0] PEDRA 
[1] PAPEL 
[2] TESOURA''')
jogador = int(input('Qual é a sua jogada? '))
print('O jogador jogou {}'.format(itens[jogador]))
print('O computador jogou {}'.format(itens[computador]))
if computador == 0:
    if jogador == 0:
        print('Empate')
    elif jogador == 1:
        print('O jogador venceu')
    elif jogador == 2:
        print('O computador venceu')
    else:
        print('Jogada inválida')
elif computador == 1:
    if jogador == 0:
        print('O computador venceu')
    elif jogador == 1:
        print('Empate')
    elif jogador == 2:
        print('O jogador venceu')
    else:
        print('Jogada inválida')
elif computador == 2:
    if jogador == 2:
        print('Empate')
    elif jogador == 1:
        print('O computador venceu')
    elif jogador == 0:
        print('O jogador venceu')
