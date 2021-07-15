from time import sleep
from random import randint
print('-'*30)
print(' '*5, 'JOGA NA MEGA SENA')
print('-'*30)
esc = int(input('Quantos jogos quer que eu sorteie? '))
lista = []
for c in range(0, esc):
    jogo = []
    while len(jogo) != 6:
        n = randint(1, 61)
        if n in jogo:
            jogo.remove(n)
        if n not in jogo:
            jogo.append(n)
    lista.append(jogo[:])
    jogo.clear()
for c in range(0, len(lista)):
    sleep(1)
    lista[c].sort()
    print(f'{c+1}º jogo: {lista[c]}')
