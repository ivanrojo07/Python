from math import sqrt

while x < 0:
  x = float(raw_input('Introduce un número positivo: '))

print 'La raíz cuadrada de %f es %f' % (x, sqrt(x))
