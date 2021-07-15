from random import randint
c = 0
pc = randint(0, 5)
while True:
    pi = str(input('Voce escolhe "Par" ou "Impar" [P/I]?')).strip().upper()[0]
    n1 = int(input('Sua escolha: '))
    if pi == 'P' and (pc + n1) % 2 == 0:
        print(f'Parabens! Eu escolhi {pc} e voce {n1} e {pc + n1} é par. Voce ganhou!')
        c += 1
    if pi == 'P' and (pc + n1) % 2 != 0:
        print(f'Eu escolhi {pc} e voce {n1} e {pc + n1} é impar. Eu ganhei!')
        break
    if pi == 'I' and (pc + n1) % 2 == 0:
        print(f'Eu escolhi {pc} e voce {n1} e {pc + n1} é par. Eu ganhei!')
        break
    if pi == 'I' and (pc + n1) % 2 != 0:
        print(f'Parabens! Eu escolhi {pc} e voce {n1} e {pc + n1} é impar. Voce ganhou!')
        c += 1
print(f'Voce me venceu {c} vezes.')
