# Pedimos la dimensión de la primera matriz y el número de columnas de la segunda.
p = int(raw_input('Dime el número de filas de A: '))
q = int(raw_input('Dime el número de columnas de A (y filas de B): '))
r = int(raw_input('Dime el número de columnas de B: '))

# Creamos dos matrices nulas...
A = []
for i in range(p):
  A.append( [0] * q )

B = []
for i in range(q):
  B.append( [0] * r )

# ... y leemos sus contenidos de teclado.
print 'Lectura de la matriz A'
for i in range(p):
  for j in range(q):
    A[i][j] = float(raw_input('Dame el componente (%d,%d): ' % (i, j)))

print 'Lectura de la matriz B'
for i in range(q):
  for j in range(r):
    B[i][j] = float(raw_input('Dame el componente (%d,%d): ' % (i, j)))
