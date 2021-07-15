imc = 0
def peso():
    imc = p / (a * a)
    if imc < 18.5:
        print(f'O IMC é {imc:.2f} e sua classificação é de Magreza e Obesidade grau 0')
    if 24.9 >= imc >= 18.5:
        print(f'O IMC é {imc:.2f} e sua classificação é Normal e Obesidade grau 0')
    if 25 <= imc <= 29.9:
        print(f'O IMC é {imc:.2f} e sua classificação é Sobrepeso e Obesidade grau 1')
    if 30 <= imc <= 39.9:
        print(f'O IMC é {imc:.2f} e sua classificação é Obesidade e Obesidade grau 2')
    if 40 <= imc:
        print(f'O IMC é {imc:.2f} e sua classificação é Obesidade Grave e Obesidade grau 3')
p = float(input('Digite o seu peso: (Kg)'))
a = float(input('Digite o sua altura: (m)'))
peso()
