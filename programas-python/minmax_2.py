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

a = minmax(10, 2, 5)
print 'El mínimo es', a[0]
print 'El máximo es', a[1]
