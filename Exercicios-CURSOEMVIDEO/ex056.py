media = 0
soma = 0
mulheres = 0
maior = 0
men = ''
for i in range(1, 5):
    print('{}ª PESSOA')
    nome = str(input('Nome: '))
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: '))
    soma += idade
    media = soma / i
    if sexo in 'Ff' and idade < 20:
        mulheres += 1
    if sexo in 'Mn':
        if idade > maior:
            maior = idade
            men = nome
print('A media do grupo foi de {}'.format(media))
print('O homem mais velho tem {} anos e se chama {}'.format(maior, men))
print('Ao todo sao {} mulheres com menos de 20 anos'.format(mulheres))
