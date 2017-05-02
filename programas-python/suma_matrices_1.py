# Pedimos la dimensión de las matrices,
m = int(raw_input('Dime el número de filas: '))
n = int(raw_input('Dime el número de columnas: '))

# Creamos dos matrices nulas...
A = []
for i in range(m):
  A.append( [0] * n )

B = []
for i in range(m):
  B.append( [0] * n )

# ... y leemos sus contenidos de teclado.
print 'Lectura de la matriz A'
for i in range(m):
  for j in range(n):
    A[i][j] = float(raw_input('Dame el componente (%d,%d): ' % (i, j)))

print 'Lectura de la matriz B'
for i in range(m):
  for j in range(n):
    B[i][j] = float(raw_input('Dame el componente (%d,%d): ' % (i, j)))
