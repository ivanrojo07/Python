cadena = raw_input('Dame una cadena: ') 
i = int(raw_input('Dame un n�mero: '))
j = int(raw_input('Dame otro n�mero: '))

if j > len(cadena):
  final = len(cadena)
else:
  final = j
subcadena = ''
for k in range(i, final):
  subcadena += cadena[k]

print 'La subcadena entre %d y %d es %s.' % (i, j, subcadena)
