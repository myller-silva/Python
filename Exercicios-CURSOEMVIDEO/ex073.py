lista = ('FLA', 'INTER', 'ATLETICO-MG', 'SP', 'FLU', 'GRE', 'PAL', 'SAN', 'ATLETICO-PR', 'BRAGANTINO', 'CE', 'CORINTHIANS', 'ATLETICO-GO', 'BH', 'SPORT', 'FOR', 'VAS', 'GOIÁS', 'CORITIBA', 'BOTAFOGO')
print(f'lista do Brasileirão: {lista}')
print(f'Os cinco primeiros são: {lista[:5]}')
print(f'Os quatro ultimos são: {lista[-4:]}')
print(f'Times em ordem alfabética: {sorted(lista)}')
print(f'O Santos está na {lista.index("SAN")+1}ª posição')
