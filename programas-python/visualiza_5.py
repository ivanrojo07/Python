# Paso 1: abrir el fichero.
fichero = open('ejemplo.txt', 'r')

# Paso 2: leer los datos del fichero.
for linea in fichero:
  print linea

# Paso 3: cerrar el fichero.
fichero.close()
