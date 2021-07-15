#Sorteando uma ordem na lista
import random
n1 = input('Primero nome: ')
n2 = input('Segundo nome: ')
n3 = input('Terceiro nome: ')
n4 = input('Quarto nome: ')
lista = [n1, n2, n3, n4]
random.shuffle(lista)  #"shuffle" significa embaralhar
print('A ordem será: {}'.format(lista))
