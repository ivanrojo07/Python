num = 7

restos_no_nulos = 0 
for divisor in range(2, num):
  if num % divisor != 0:
    restos_no_nulos += 1

if restos_no_nulos == num - 2:
  print 'El n�mero', num, 'es primo'
else:
  print 'El n�mero', num, 'no es primo'
