a = int(raw_input('Dame el primer número: '))
b = int(raw_input('Dame el segundo número: '))
c = int(raw_input('Dame el tercer número: '))

if a >= b and a >= c:
  maximo = a
if b >= a and b >= c:
  maximo = b
if c >= a and c >= b:
  maximo = c
print 'El máximo es', maximo
