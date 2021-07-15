from time import sleep


def contador(inicio, fim, passo):
    if passo == 0:
        passo = 1
    elif passo < 0:
        passo *= -1
    print(f"Contando de {inicio} até {fim} de {passo} em {passo}.")
    if inicio < fim:
        while True:
            sleep(.5)
            print(inicio, end=' ')
            inicio += passo
            if inicio > fim:
                break
    elif inicio > fim:
        while True:
            sleep(.5)
            print(inicio, end=' ')
            inicio -= passo
            if inicio < fim:
                break
    print("FIM!")


contador(0, 10, 1)
contador(10, 0, 1)
print('Agora é sua vez de personalizar a contagem!')
lista = [int(input('Inicio: ')), int(input('Fim: ')), int(input('Passo: '))]
contador(lista[0], lista[1], lista[2])
