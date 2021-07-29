me = float(input("Media final: "))

conceito : str='invalido'

if 0 <= me < 5:
    conceito = 'D'
elif 5 <= me < 7:    
    conceito = 'C'
elif 7 <= me < 9:    
    conceito = 'B'
elif 9 <= me <=10:    
    conceito = 'A'

print(f"Conceito: {conceito}")
