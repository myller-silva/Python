#Índice de Massa Corporal
peso = float(input('Qual seu peso? (Kg) '))
altura = float(input('Qual sua altura? (m) '))
imc = peso / (altura**2)
print('O seu IMC é: {:.1f}'.format(imc))
if imc < 18.5:
    print('Abaixo do peso ideal')
elif imc < 25:
    print('Peso normal')
elif imc < 30:
    print('Sobrepeso')
elif imc < 35:
    print('Obesidade grau I')
elif imc < 40:
    print('Obesidade grau II')
else:
    print('Obesidade grau III ou Mórbida')