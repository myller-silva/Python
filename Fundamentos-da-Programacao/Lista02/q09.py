n1 = int(input("Primeiro valor: "))
n2 = int(input("Segundo valor: "))
c = str(input("Operação: "))


if c=='+':
    r = n1+n2
elif c=='-':
    r = n1-n2
elif c=='*':
    r = n1*n2
elif c=='/' and n2!=0:
    r = n1/n2
else:
    r = 'operação invalida'


print(r)
