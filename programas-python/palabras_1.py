cadena = raw_input('Escribe una frase: ') 
while cadena != '':
  blancos = 0
  for caracter in cadena:
    if caracter == ' ':
      blancos += 1
  palabras = blancos + 1 # Hay una palabra m�s que blancos
  print 'Palabras:', palabras

  cadena = raw_input('Escribe una frase: ')
