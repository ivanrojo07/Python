try:
  fichero = open('ejemplo.txt', 'r')
  for linea in fichero:
    print linea
  fichero.close()
except IOError:
  print 'El fichero no existe.'
