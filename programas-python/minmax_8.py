def minmax(a, b, c):
  if a < b:
    if a < c:
      min = a
    else:
      min = c
  else:
    if b < c:
      min = b
    else:
      min = c
  if a > b:
    if a > c:
      max = a
    else:
      max = c
  else:
    if b > c:
      max = b
    else:
      max = c
  return [min, max]

[minimo, maximo] = minmax(10, 2, 5)
print 'El mínimo es', minimo
print 'El máximo es', maximo
