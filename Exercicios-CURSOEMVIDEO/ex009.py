#ler um numero inteiro qualquer e imprimir a tabuada dele
n = int(input('Digite um número: '))

print('A tabuada do {} é: '.format(n))
for i in range(1, 11):
  print('{}x{} = {}'.format(n, i, n*i))
