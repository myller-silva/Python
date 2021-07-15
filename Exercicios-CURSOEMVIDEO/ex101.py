def voto(anonascimento):
    from datetime import date
    idade = date.today().year - anonascimento
    print(f"Sua idade é {idade}. Portanto, ", end='')
    if idade < 16:
        print(f'voto negado.')
    elif 16 <= idade < 18 or 65 <= idade:
        print(f'voto opcional.')
    elif 18 <= idade:
        print(f'voto obrigatório. ')


n = int(input("Ano de nascimento: "))
voto(n)
