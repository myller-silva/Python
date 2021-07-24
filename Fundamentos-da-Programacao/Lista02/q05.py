# Escrever um algoritmo para ler dois valores numéricos e apresentar a diferença do maior pelo menor.

n = []

n.append( float(input("Digite o primeiro numero: ")) )
n.append( int(input("Digite o primeiro numero: ")) )

print(f"\n{ max(n) } - { min(n) } = { max(n)-min(n) }\n")

