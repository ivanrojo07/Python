a = int(raw_input('Dame el primer n�mero: '))
b = int(raw_input('Dame el segundo n�mero: '))
c = int(raw_input('Dame el tercer n�mero: '))

if a >= b and a >= c:
  maximo = a
if b >= a and b >= c:
  maximo = b
if c >= a and c >= b:
  maximo = c
print 'El m�ximo es', maximo
