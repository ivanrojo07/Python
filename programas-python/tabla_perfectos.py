def es_perfecto(n): # Averigua si el n�mero $n$ es o no es perfecto.
  sumatorio = 0
  for i in range(1, n):
    if n % i == 0:
      sumatorio += i
  return sumatorio == n

def tabla_perfectos(m): # Muestra todos los n�meros perfectos entre 1 y $m$.
  for i in range(1, m+1):
    if es_perfecto(i):
      print i, 'es un n�mero perfecto'

numero = int(raw_input('Dame un n�mero: '))
resultado = tabla_perfectos(100)
print resultado
