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
