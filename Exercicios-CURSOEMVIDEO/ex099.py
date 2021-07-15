from time import sleep
def maior(lst):
    print("A analisando os valores passados...")
    for elemento in lst:
        sleep(.5)
        print(elemento, end=' ')
    print(f"\nForam {len(lst)} valores ao todo.")
    if len(lst) == 0:
        print(f"O maior valor não existe")
    print(f"O maior valor informado foi: {max(lst)}")


lista = [45, 8, 89, 51, 6, 2]
maior(lista)
