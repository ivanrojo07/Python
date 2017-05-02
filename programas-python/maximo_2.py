a = int(raw_input('Dame el primer número: '))
b = int(raw_input('Dame el segundo número: '))

if a > b:
  maximo = a
if b > a:
  maximo = b

print 'El máximo es', maximo
