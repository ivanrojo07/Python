def invierte(lista):
  for i in range(len(lista)/2):
    c = lista[i]
    lista[i] = lista[len(lista)-1-i]
    lista[len(lista)-1-i] = c

a = [1, 2, 3, 4]
invierte(a)
print a
