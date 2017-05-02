from math import sqrt

a = float(raw_input('Valor de a: '))
b = float(raw_input('Valor de b: '))
c = float(raw_input('Valor de c: '))

if a == 0 and b == 0 and c == 0:
   print 'La ecuación tiene infinitas soluciones.'      
else:
  if a == 0 and b == 0:
    print 'La ecuación no tiene solución.'
  else:
    if a == 0:
      x = -c / b
      print 'Solución de la ecuación: x=%4.3f' % x
    else:
      x1 = (-b + sqrt(b**2 - 4*a*c)) / (2 * a)
      x2 = (-b - sqrt(b**2 - 4*a*c)) / (2 * a)
      print 'Soluciones de la ecuación: x1=%4.3f y x2=%4.3f' % (x1, x2)
