# revisa a aula do curso em video de manipulação de string

frase = str(input('Digite uma frase: ')).strip().upper()  #strip tira os espaços e upper torna maiusculo
palavras = frase.split() # split separa a frase pelos dos espaços
junto = ''.join(palavras) # join junta strings e se escolhe o que vai as separar
inverso = ''
