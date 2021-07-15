lista = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito','dezenove', 'vinte')
while True:
    n = int(input('digite um número entre 0 e 20: '))
    if 0 <= n <= 20:
        print(f'voce digitou {lista[n]}')
        break
    else:
        print(f'o numero {n} nao está entre 0 e 20. tente novamente.', end=' ')
