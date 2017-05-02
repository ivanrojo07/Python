def integral_x2(a, b, n):
  deltax = (b-a) / n
  sumatorio = 0
  for i in range(n):
    sumatorio += deltax * (a + i * deltax) ** 2
  return sumatorio
