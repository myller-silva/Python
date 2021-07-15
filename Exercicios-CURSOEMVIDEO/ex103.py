def ficha(nome='', gols=''):
    if nome == '':
        nome = '<desconhecido>'
    if gols == '':
        gols = '0'
    print(f"O jogador {nome} fez {gols} gol(s)")


lista = [str(input('Nome do jogador: ')), str(input('Gols marcados: '))]
ficha(lista[0], lista[1])
