num = int(raw_input('Dame un n�mero: '))

creo_que_es_primo = True
for divisor in range(2, num):
  if num % divisor == 0:
    creo_que_es_primo = False
    break

if creo_que_es_primo:
  print 'El n�mero', num, 'es primo'
else:
  print 'El n�mero', num, 'no es primo'
