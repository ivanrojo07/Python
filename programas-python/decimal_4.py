bits = raw_input('Dame un n�mero binario: ')

valor = 0
for bit in bits:
  if bit == '1':
    valor = 2 * valor + 1
  else:
    valor = 2 * valor

print 'Su valor decimal es', valor
