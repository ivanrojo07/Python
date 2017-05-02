def exponencial(a, n):
  sumatorio = 0.0
  for k in range(n):
    # C�lculo de $a^k$.
    numerador = 1.0
    for i in range(1, k+1):
      numerador *= a
    # Adici�n de nuevo sumando al sumatorio.
    sumatorio += numerador / k!
  return sumatorio
