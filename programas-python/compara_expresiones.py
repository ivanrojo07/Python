n = int(raw_input('Dame un n�mero: ')) 
m = int(raw_input('Dame otro n�mero: '))

if n * m == 100:
  print 'El producto %d * %d es igual a 100' % (n, m)
if n * m != 100:
  print 'El producto %d * %d es distinto de 100' % (n, m)
