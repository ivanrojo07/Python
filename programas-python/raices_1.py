numero = float(raw_input('Dame un n�mero: '))

for n in range(2, 101):
  print 'la ra�z %d-�sima de %f es %f' % (numero, n, numero**(1.0/n)) 
