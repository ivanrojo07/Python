def elevado(a, k):
  productorio = 1.0
  for i in range(1, k+1):
    productorio *= a
  return productorio

def factorial(k):
  productorio = 1.0
  for i in range(1, k+1):
    productorio *= i
  return productorio

def exponencial(a, n):
  sumatorio = 0.0
  for k in range(n):
    sumatorio += elevado(a, k) / factorial(k)
  return sumatorio
