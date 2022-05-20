from math import pi;
from math import pow;

def volumeEsfera(r):
  return( (4*pi*pow(r, 3)) / 3 );

r = int(input("Raio: "));
v = volumeEsfera(r);
print(pi)
print(v)