def exponencial(a, n):
  sumatorio = 0.0
  for k in range(n):
    sumatorio += a**k / (k!)
  return sumatorio
