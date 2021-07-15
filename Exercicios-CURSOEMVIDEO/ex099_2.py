from time import sleep
def maior(*num):
    maior = 0
    print(f"Analisando os valores... ")
    for c in range(0, len(num)):
        sleep(.5)
        print(num[c], end=' ')
        if c == 0:
            maior = num[c]
        elif num[c] > maior:
            maior = num[c]
    print(f"O maior valor é {maior}")
maior(2, 9, 4, 5, 7, 2)
