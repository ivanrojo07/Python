a = float(raw_input('Valor de a: '))
b = float(raw_input('Valor de b: '))

if a != 0:
  x = -b/a
  print 'Soluci�n: ', x
if a == 0:   
  if b != 0:
    print 'La ecuaci�n no tiene soluci�n.'   
  if b == 0:
    print 'La ecuaci�n tiene infinitas soluciones.' 
