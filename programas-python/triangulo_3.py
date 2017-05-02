from math import sqrt

def area_triangulo(a, b, c):
  s = (a + b + c) / 2.0
  return sqrt(s * (s-a) * (s-b) * (s-c))

print area_triangulo(1, 3, 2.5)
print s
