from random import randint
from time import sleep


def sorteia(lista):
    print("Sorteando os 5 valores:", end=' ')
    for c in range(0, 5):
        sleep(.5)
        lista.append(randint(0, 10))
        print(lista[c], end=' ')
    print("PRONTO!")


def somaPar(lista):
    somapares = 0
    for elemento in lista:  #varrendo o vetor
        if elemento % 2 == 0:
            somapares += elemento
    print(f"Somando os valores pares de {lista}, temos {somapares}")


numeros = []
sorteia(numeros)
somaPar(numeros)
