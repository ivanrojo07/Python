def sin_repetidos(lista):
  resultado = []
  for elemento in lista:
    if elemento not in resultado:
      resultado.append(elemento)
  return resultado
