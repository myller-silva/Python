def notas(*num, situacao=False):
    quantidade = maior = media = 0
    for elemento in num:
        quantidade += 1
        if quantidade == 1:
            maior = elemento
        elif elemento > maior:
            maior = elemento
    for elemento in num:
        media += elemento/quantidade
    dicionario = {'Total': quantidade, 'Maior': maior, 'Media': media}
    if situacao:
        if 10 > media >= 7:
            dicionario['Situação'] = ' boa'
        elif media < 7:
            dicionario['Situação'] = 'ruim'
    for k, v in dicionario.items():
        print(f"{k:.<9}{v:.>17}")

notas(3, 5, 7, situacao=True)
#help(notas())
