import math;

def anDeUmaPG(a1, q, n):
  return a1*math.pow(q, n-1);

a1 = int(input("a1: "));
q = int(input("q: "));
n = int(input("n: "));
an = anDeUmaPG(a1, q, n);

print(an);
