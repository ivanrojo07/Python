cadena = raw_input('Escribe una frase: ') 
while cadena != '':
  cambios = 0
  anterior = ''
  for caracter in cadena:
    if caracter == ' ' and anterior != ' ':
      cambios += 1
    anterior = caracter
  palabras = cambios + 1 # Hay una palabra más que cambios de no blanco a blanco
  print 'Palabras:', palabras 

  cadena = raw_input('Escribe una frase: ')
