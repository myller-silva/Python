def sistema(msg):
    print(f"{help(msg)}")

while True:
    resposta = str(input('\033[4;43mInterative help: '))
    if resposta in 'FIMfimFim':
        break
    sistema(resposta)
