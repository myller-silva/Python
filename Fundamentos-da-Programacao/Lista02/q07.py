mes = ["janeiro", "fevereiro", "março", "abril", "maio", "junho", "julho", "agosto", "setembro", "outubro", "novembro", "dezembro"]

n = int(input("Digite um numero: "))

if 0>n or n>12:
    print("Mês inválido")
else:
    print(f"{n} corresponde ao mês {mes[n-1]}")
