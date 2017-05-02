from math import sqrt

a = float(raw_input('Valor de a: '))
b = float(raw_input('Valor de b: '))
c = float(raw_input('Valor de c: '))

if a == 0:
  if b == 0:
    if c == 0:
      print 'La ecuaci�n tiene infinitas soluciones.'      
    else:
      print 'La ecuaci�n no tiene soluci�n.'
  else:
    x = -c / b
    print 'Soluci�n de la ecuaci�n: x=%4.3f' % x
else:
  x1 = (-b + sqrt(b**2 - 4*a*c)) / (2 * a)
  x2 = (-b - sqrt(b**2 - 4*a*c)) / (2 * a)
  print 'Soluciones de la ecuaci�n: x1=%4.3f y x2=%4.3f' % (x1, x2)
