def leiaint(msg):
    global n
    while True:
        n2 = input(msg)
        if n2.isnumeric():
            n = n2
            return n
        else:
            print('\033[31mERRO. Digite um número inteiro válido.')


n = leiaint('\033[mNumero: ')
print(f"\033[34mVoce digitou o número: {n}")
