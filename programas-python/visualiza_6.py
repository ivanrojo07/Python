import os

if os.path.exists('ejemplo.txt'):
  fichero = open('ejemplo.txt', 'r')
  for linea in fichero:
    print linea
  fichero.close()
else:
  print 'El fichero no existe.'
