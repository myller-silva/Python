while True:
    n1 = int(input('Quer ve a tabuada de qual numero ?'))
    if n1 < 0:
        break
    for c in range(1, 11):
        p = n1 * c
        print(f'{n1} x {c} = {p}')
