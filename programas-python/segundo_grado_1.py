from math import sqrt  # \emph{sqrt} calcula la ra�z cuadrada.

a = float(raw_input('Valor de a: '))
b = float(raw_input('Valor de b: '))
c = float(raw_input('Valor de c: '))

x1 = (-b + sqrt(b**2 - 4*a*c)) / (2 * a)
x2 = (-b - sqrt(b**2 - 4*a*c)) / (2 * a)

print 'Soluciones de la ecuaci�n: x1=%4.3f y x2=%4.3f' % (x1, x2)
