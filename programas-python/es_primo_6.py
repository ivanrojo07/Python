num = int(raw_input('Dame un número: '))

creo_que_es_primo = True
divisor = 2
while divisor < num:
  if num % divisor == 0:
    creo_que_es_primo = False
  divisor += 1

if creo_que_es_primo:
  print 'El número', num, 'es primo'
else:
  print 'El número', num, 'no es primo'
