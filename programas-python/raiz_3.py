from math import sqrt

x = float(raw_input('Introduce un n�mero positivo: '))
while x < 0:
  x = float(raw_input('Introduce un n�mero positivo: '))

print 'La ra�z cuadrada de %f es %f' % (x, sqrt(x))
