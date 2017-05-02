def integral_x2(a, b, n):
  if n == 0:
    sumatorio = 0
  else:
    deltax = (b-a) / n
    sumatorio = 0
    for i in range(n):
      sumatorio += deltax * (a + i * deltax) ** 2
  return sumatorio
