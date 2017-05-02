def exponencial(a, n):
  sumatorio = 0.0
  for k in range(n):
    # C�lculo de $a^k$.
    numerador = 1.0
    for i in range(1, k+1):
      numerador *= a
    # C�lculo de $k!$.
    denominador = 1.0
    for i in range(1, k+1):
      denominador *= i
    # Adici�n de nuevo sumando al sumatorio.
    sumatorio += numerador / denominador
  return sumatorio
