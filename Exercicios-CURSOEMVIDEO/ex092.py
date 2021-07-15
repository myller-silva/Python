import datetime
cad = {}
cad['nome'] = str(input('Nome: '))
nasc = int(input('Ano de nascimento: '))
cad['idade'] = datetime.date.today().year - nasc
carteira = int(input('Carteira de trabalho: [0 = não tem]'))
if carteira != 0:
    cad['carteira'] = carteira
    cad['contratacao'] = int(input('Ano de contratação: '))
    cad['salario'] = float(input('Salario: '))
    cad['aposentadoria será aos'] = (cad['contratacao'] + 35) - nasc
for k, v in cad.items():
    print(f' - {k}: {v}')
