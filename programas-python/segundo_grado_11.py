from math import sqrt

a = float(raw_input('Valor de a: '))
b = float(raw_input('Valor de b: '))
c = float(raw_input('Valor de c: '))

try:
  x1 = (-b + sqrt(b**2 - 4*a*c)) / (2 * a)
  x2 = (-b - sqrt(b**2 - 4*a*c)) / (2 * a)
  if x1 == x2:
    print 'Soluci�n de la ecuaci�n: x=%4.3f' % x1
  else:
    print 'Soluciones de la ecuaci�n: x1=%4.3f y x2=%4.3f' % (x1, x2)
except:
  # No sabemos si llegamos aqu� por una divisi�n por cero o si llegamos
  # por intentar calcular la ra�z cuadrada de un discriminante negativo.
  print 'O no hay soluciones reales o es una ecuaci�n de primer grado'
