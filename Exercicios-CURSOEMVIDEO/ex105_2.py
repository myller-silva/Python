def notas(*num, situacao=False):
    notas = {'Total': len(num), 'Maior': max(num), 'Menor': min(num), 'Média': sum(num)/len(num)}
    if situacao:
        if notas['Média'] >= 7:
            notas['Situação'] = 'Boa'
        elif notas['Média'] < 7:
            notas['Situação'] = 'Ruim'
    for k, v in notas.items():
        print(f"{k:.<9}{v:.>17}")


notas(3, 5, 7, situacao=True)
print()
notas(7, 8, 9, 6, situacao=True)
