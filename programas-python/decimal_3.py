bits = raw_input('Dame un n�mero binario: ')

valor = 0
for bit in bits:
  valor += valor + int(bit)

print 'Su valor decimal es', valor
