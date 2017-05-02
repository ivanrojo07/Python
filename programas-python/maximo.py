def maximo(lista):
  if len(lista) > 0:
    candidato = lista[0]
    for elemento in lista:
      if elemento > candidato:
        candidato = elemento
  else:
    candidato = None
  return candidato  
