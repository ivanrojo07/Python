a = float(raw_input('Valor de a: '))
b = float(raw_input('Valor de b: '))

try:
  x = -b/a
  print 'Soluci�n: ', x
except:
  if b != 0:
    print 'La ecuaci�n no tiene soluci�n.'   
  else:
    print 'La ecuaci�n tiene infinitas soluciones.' 
