dicio = {'nome': str(input('Nome: ')).upper(), 'nota': float(input('Nota: '))}
if 0 <= dicio['nota'] < 7:
    dicio['situacao'] = 'Reprovado'
elif 7 <= dicio['nota'] <= 10:
    dicio['situacao'] = 'Aprovado'
else:
    print('nota inválida')
print(f'O aluno {dicio["nome"]} foi {dicio["situacao"]}')
