num = int(input('Digite um numero inteiro: '))
print('''Escolha uma das bases de conversao
[1] converter para binario
[2] converter para octal
[3] converter para hexadecimal''')
escolha = int(input('Sua escolha: '))
if escolha == 1:
    print('O numero {} em binário é {}'.format(num, bin(num)[2:]))  # [2:] significa fatiar a str apos a 2ªletra
elif escolha == 2:
    print('O numero {} em octal é {}'.format(num, oct(num)[2:]))
elif escolha == 3:
    print('O numero {} em hexadecimal é {}'.format(num, hex(num)[2:]))
else:
    print('Opção inválida.')
