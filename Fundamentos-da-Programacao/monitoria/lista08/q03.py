def mdc(n1, n2):
  mdc = 1
  i = 2
  while (i<n1 and i<n2):
    while( n1 % i == 0 and n2 % i == 0 ):
      mdc *= i
      n1 = n1 / i
      n2 = n2 / i
    i+=1
  
  return mdc

print(">>> Calcular MDC <<<")
n1 = int(input("n1: "))
n2 = int(input("n2: "))
print(f"MDC ({n1} e {n2}) = {mdc(n1, n2)}")
