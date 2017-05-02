def fibonacci(n):
  if n==1 or n==2:
    resultado = 1
  elif n > 2:
    resultado = fibonacci(n-1) + fibonacci(n-2)
  return resultado
