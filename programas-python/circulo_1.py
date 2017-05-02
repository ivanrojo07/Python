from math import pi

radio = float(raw_input('Dame el radio de un círculo: '))

# Menú
print 'Escoge una opción: '
print 'a) Calcular el diámetro.'
print 'b) Calcular el perímetro.'
print 'c) Calcular el área.'
opcion = raw_input('Teclea a, b o c y pulsa el retorno de carro: ')

if opcion == 'a':  # Cálculo del diámetro.
  diametro = 2 * radio
  print 'El diámetro es', diametro
else:
  if opcion == 'b': # Cálculo del perímetro.
    perimetro = 2 * pi * radio
    print 'El perímetro es', perimetro
  else:
    if opcion == 'c': # Cálculo del área.
     area = pi * radio ** 2
     print 'El área es', area 
