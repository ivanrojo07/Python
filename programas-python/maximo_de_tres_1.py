a = int(raw_input('Dame el primer número: '))
b = int(raw_input('Dame el segundo número: '))
c = int(raw_input('Dame el tercer número: '))

if a > b:
  if a > c:
    maximo = a
  else:
    maximo = c
else:
  if b > c:  
    maximo = b
  else:
    maximo = c

print 'El máximo es', maximo
