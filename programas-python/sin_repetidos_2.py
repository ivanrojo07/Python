def sin_repetidos(lista):
  resultado = []
  for elemento in lista:
    if elemento not in resultado:
      resultado.append(elemento)
  return resultado

una_lista = sin_repetidos([1, 2, 1, 3, 2])
print una_lista
