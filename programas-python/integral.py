def integral_x2(a, b, n):
  if n == 0:
    sumatorio = 0
  else:
    deltax = (b-a) / float(n)
    sumatorio = 0
    for i in range(n):
      sumatorio += deltax * (a + i * deltax) ** 2
  return sumatorio

inicio = float(raw_input('Inicio del intervalo: '))
final = float(raw_input('Final del intervalo: '))
partes = int(raw_input('Número de rectángulos: '))

print 'La integral de x**2 entre %f y %f' % (inicio, final),
print 'vale aproximadamente %f' % integral_x2(inicio, final, partes)
