car = raw_input('Dame un car�cter: ')

if 'a' <= car.lower() <= 'z'  or  car == '_':
  print 'Este car�cter es v�lido en un identificador en Python.'
else:
  if not (car < '0'  or  '9' < car):
    print 'Un d�gito es v�lido en un identificador en Python,',
    print 'siempre que no sea el primer car�cter.'
  else:
    print 'Car�cter no v�lido para formar un identificador en Python.'
