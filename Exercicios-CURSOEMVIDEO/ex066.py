c = s = 0
while True:
    n1 = int(input('Digite um numero: [999 para parar] '))
    if n1 == 999:
        break
    c += 1
    s += n1
print(f'Foram digtados {c} numeros e a soma deles é {s}')
