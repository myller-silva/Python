import math;

a = int(input("Digite o valor de a: "));
b = int(input("Digite o valor de b: "));
c = int(input("Digite o valor de c: "));

delta = b*b - 4*a*c;
print(f"delta: {delta}");
if(delta<0):
  exit(1);

denominador = 2*a;
numerador1 = b*(-1) - math.pow(delta, 0.5);
numerador2 = b*(-1) + math.pow(delta, 0.5);


r1 = numerador1 / denominador;
r2 = numerador2 / denominador;

sinalB=""
sinalC=""
if(b<0):
  sinalB="-"
  b = b*(-1)
else:
  sinalB = "+"

if(c<0):
  sinalC="-"
  c = c*(-1)
else:
  sinalC = "+"

print(f"expressao: {a}x^2 {sinalB} {b}x {sinalC} {c}")
print(f"raiz 1: {r1}")
print(f"raiz 2: {r2}")

