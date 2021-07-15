def escreva(msg):
    num = len(msg)
    print(f"{'~'*(num+4)}")
    print(f"  {msg}")
    print(f"{'~'*(num+4)}")


escreva(input('Mensagem: '))
