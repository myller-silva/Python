#ler o salário de um funcionario e mostrar seu novo salario com 15 porcento de aumento
sal = float(input('Salário do funcionário: '))
aumento = 0.15
saldesc = sal*(1+aumento)
print('O salário do funcionário com aumento é: {} '.format(saldesc))
