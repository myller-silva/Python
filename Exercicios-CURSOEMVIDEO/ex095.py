lista = []
while True:
    dicio = {}
    dicio['nome'] = str(input('Nome do jogador: '))
    dicio['partidas'] = int(input(f'Quantas partidas {dicio["nome"]} jogou? '))
    gols = []
    for c in range(0, dicio['partidas']):
        gols.append(int(input(f'Quantos gols fez na {c+1}º?')))
    dicio['gols'] = gols[:]
    gols.clear()
    lista.append(dicio.copy())
    dicio.clear()
    esc = ' '
    while esc not in 'SN':
        esc = str(input('quer continuar? ')).upper().strip()[0]
    if esc == 'N':
        break
print('-='*30)
print(f"cad {'nome':<10}{'gols':<10}{'total':>20}")
for c in range(0, len(lista)):
    print(c, f'  {lista[c]["nome"]:<10}{lista[c]["gols"]}', f"{sum(lista[c]['gols']):>30}")
