def nota(c):
    a = float(c)
    if 0 <= a <= 10.0:
        media = a
        if 0 <= a <= 4.9:
            print('Media de conceito D')
        if 5.0 <= a <= 6.9:
            print('Media de conceito C')
        if 7.0 <= a <= 8.9:
            print('Media de conceito B')
        if 9.0 <= a <= 10.0:
            print('Media de conceito A')
    else:
        print('Media invalida')
    return a
a = input('Media do aluno: ')
print(nota(a))
