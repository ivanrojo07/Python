nombre = raw_input('Nombre del fichero: ')
fichero = open(nombre, 'r')

texto = ''
while 1:
  caracter = fichero.read(1)
  if caracter == '':
    break
  elif caracter >= 'a' and caracter <='y':
    texto += chr(ord(caracter) + 1)
  elif caracter == 'z':
    texto += 'a'
  else:
    texto += caracter
fichero.close()
print texto
