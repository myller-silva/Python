# crie um programa que leia um numero e mostre sua parte inteira
from math import trunc
n = float(input('Digite um número: '))
print('O valor digitado foi {} e sua parte inteira é {}'.format(n, trunc(n)))
# print('O valor digitado foi {} e sua parte inteira é {}'.format(n, int(n)))
