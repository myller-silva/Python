notas10 = notas1 = notas5 = notas20 = notas50 = 0
saque = int(input('Qual valor voce quer sacar? RS'))
while saque >= 50:
    saque -= 50
    notas50 += 1
while saque >= 20:
    saque -= 20
    notas20 += 1
while saque >= 10:
    saque -= 10
    notas10 += 1
while saque >= 5:
    saque -= 5
    notas5 += 1
while saque >= 1:
    saque -= 1
    notas1 += 1
print(f'notas de R$50: {notas50}. ' if notas50 != 0 else '', end='')
print(f'notas de R$20: {notas20}. ' if notas20 != 0 else '', end='')
print(f'notas de R$10: {notas10}. ' if notas10 != 0 else '', end='')
print(f'notas de R$5: {notas5}. ' if notas5 != 0 else '', end='')
print(f'notas de R%1: {notas1}. ' if notas1 != 0 else '')
