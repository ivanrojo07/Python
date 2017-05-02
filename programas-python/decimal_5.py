bits = raw_input('Dame un número binario: ')

valor = 0
for bit in bits:
  if bit == '1':
    valor += valor  + 1
  else:
    valor += valor

print 'Su valor decimal es', valor
