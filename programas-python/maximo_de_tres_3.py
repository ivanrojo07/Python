a = int(raw_input('Dame el primer n�mero: '))
b = int(raw_input('Dame el segundo n�mero: '))
c = int(raw_input('Dame el tercer n�mero: '))

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

print 'El m�ximo es', maximo
