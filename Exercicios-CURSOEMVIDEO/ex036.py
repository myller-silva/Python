#Aprovando Empréstimo
casa = float(input('Valor da casa R$'))
salario = float(input('Salario do comprador R$'))
anos = float(input('Quantos anos de financiamento? '))
prestacao = casa / (anos * 12)
minimo = 0.3 * salario
print('Para pagar uma casa de R${:.2f} em {} anos a prestacao será de R${:.2f}'.format(casa, anos, prestacao))
if prestacao <= minimo:
    print('Emprestimo pode ser CONCEDIDO!')
else:
    print('Emprestimo negado!')
