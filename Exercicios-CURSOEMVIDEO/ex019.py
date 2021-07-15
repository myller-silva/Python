#Sorteando um item na lista
import random  #ou posso usar: from random import choices . e eliminar as referencias a random
n1 = str(input('Primeiro aluno: '))
n2 = input('Segundo aluno: ')
n3 = input('Terceiro aluno: ')
n4 = input('Quarto aluno: ')
lista = [n1, n2, n3, n4]
escolhido = random.choice(lista)
print('O aluno escolhido foi {}.'.format(escolhido))