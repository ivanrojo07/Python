from math import pi

radio = float(raw_input('Dame el radio de un c�rculo: '))

# Men�
print 'Escoge una opci�n: '
print 'a) Calcular el di�metro.'
print 'b) Calcular el per�metro.'
print 'c) Calcular el �rea.'
opcion = raw_input('Teclea a, b o c y pulsa el retorno de carro: ')

if opcion == 'a':  # C�lculo del di�metro.
  diametro = 2 * radio
  print 'El di�metro es', diametro
else:
  if opcion == 'b': # C�lculo del per�metro.
    perimetro = 2 * pi * radio
    print 'El per�metro es', perimetro
  else:
    if opcion == 'c': # C�lculo del �rea.
     area = pi * radio ** 2
     print 'El �rea es', area 
