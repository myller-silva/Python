from random import randint; from time import sleep; from operator import itemgetter
jogodado = {'Jogador 1': randint(1, 6), 'Jogador 2': randint(1, 6), 'Jogador 3': randint(1, 6),
            'Jogador 4': randint(1, 6)}
ranking = {}
print('Valores sorteados: ')
for k, v in jogodado.items():
    print(f'o {k} tirou {v}')
    sleep(1)
ranking = sorted(jogodado.items(), key=itemgetter(1))
print('VENCEDORES: ')
for k, v in ranking:
    print(f'{k} com {v}')
    sleep(1)
