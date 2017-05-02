nombre_entrada = raw_input('Nombre del fichero de entrada: ')
nombre_salida = raw_input('Nombre del fichero de salida: ')

f_entrada = open(nombre_entrada, 'r')
f_salida = open(nombre_salida, 'w')

for linea in f_entrada:
  nueva_linea = ''
  for caracter in linea:
    if caracter >= 'a' and caracter <='y':
      nueva_linea += chr(ord(caracter) + 1)
    elif caracter == 'z':
      nueva_linea += 'a'
    else:
      nueva_linea += caracter
  f_salida.write(nueva_linea)

f_entrada.close()
f_salida.close()
