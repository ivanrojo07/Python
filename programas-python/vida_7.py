 filas = 10
columnas = 10

tablero = []
for i in range(filas):
  tablero.append([0]*columnas)

tablero[4][5] = 1
tablero[5][5] = 1
tablero[6][5] = 1

for y in range(filas):
  for x in range(columnas):
    if tablero[y][x]:
      print '*',
    else:
      print '.',
  print

pulsos = 10
for t in range(pulsos): 
  # Actualizar el tablero.
  for y in range(filas):
    for x in range(columnas):
      # Calcular el número de vecinos de la celda que estamos visitando.
      n = 0
      if tablero[y-1][x-1]: 
        n += 1
      if tablero[ y ][x-1]: 
        n += 1
      if tablero[y+1][x-1]: 
        n += 1
      if tablero[y-1][ x ]: 
        n += 1
      if tablero[y+1][ x ]: 
        n += 1
      if tablero[y-1][x+1]: 
        n += 1
      if tablero[ y ][x+1]: 
        n += 1
      if tablero[y+1][x+1]: 
        n += 1
      # Aplicar las reglas.
      if   tablero[y][x] and (n == 2 or n == 3):   # Supervivencia
        tablero[y][x] = 1
      elif not tablero[y][x] and n == 3:     # Nacimiento
        tablero[y][x] = 1
      else:                     # Superpoblación y aislamiento
        tablero[y][x] = 0
  # Representar el tablero.
  for y in range(filas):
    for x in range(columnas):
      if tablero[y][x]:
        print '*',
      else:
        print '.',
    print
