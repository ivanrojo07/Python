from math import pi

radio = float(raw_input('Dame el radio de un c�rculo: '))

print 'Escoge una opci�n: '
print 'a) Calcular el di�metro.'
print 'b) Calcular el per�metro.'
print 'c) Calcular el �rea.'
opcion = raw_input('Teclea a, b o c y pulsa el retorno de carro: ')

if opcion == 'a': 
  diametro = 2 * radio
  print 'El di�metro es', diametro
else:
  if opcion == 'b':
    perimetro = 2 * pi * radio
    print 'El per�metro es', perimetro
  else:
    if opcion == 'c':
      area = pi * radio ** 2
      print 'El �rea es', area
    else:
      print 'S�lo hay tres opciones: a, b o c.'
      print 'T� has tecleado', opcion
