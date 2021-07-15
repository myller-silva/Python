dados = {}
dados['nome'] = str(input('Nome do jogador: '))
dados['partidas'] = int(input(f'Quantas partidas {dados["nome"]} jogou? '))
gols = []
for c in range(0, dados['partidas']):
    n = int(input(f'Quantas gols na {c+1}º partida? '))
    gols.append(n)
dados['gols'] = gols[:]
dados['soma de gols'] = sum(gols[:])  # sum(lista[]) soma os elementos da lista
gols.clear()
print('-='*40)
print(dados)
print('-='*40)
for k, v in dados.items():
    print(f'{k}: {v}')
print('-='*40)
print(f'o jogador {dados["nome"]} jogou {dados["partidas"]} jogos.')
for c in range(0, dados['partidas']):
    print(f'na {c+1}º partida, fez {dados["gols"][c]} gols.')
print(f'no total foram: {dados["soma de gols"]} gols')
