def modifica_parametros(x, y):
  x = 1
  y.append(3)
  y = y + [4]
  y[0] = 10

a = 0
b = [0, 1, 2]
modifica_parametros(a, b)
print a
print b
