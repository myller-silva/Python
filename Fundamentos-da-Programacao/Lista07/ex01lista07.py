def soma(n1, n2):
    return n1 + n2
def sub(n1, n2):
    return n1 - n2
def div(n1, n2):
    return n1/n2
def mult(n1, n2):
    return n1*n2
n = float(input('O valor 1: '))
n0 = float(input('O valor de: '))
c = (input('Qual operaçao que fazer? [+, -, /, *]'))
if c == '-' or c == '+' or c == '/' or c == '*':
    if c == "+":
        print(f'{n} + {n0} = {soma(n, n0)}')
    if c == "-":
        print(f'{n} - {n0} = {sub(n, n0)}')
    if c == "/":
        print(f'{n} / {n0} = {div(n, n0)}')
    if c == "*":
        print(f'{n} * {n0} = {mult(n, n0)}')
else:
    print('Operaçao inválida')
