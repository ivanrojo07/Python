def menu():
  opcion = ''
  while len(opcion) != 1 or opcion not in 'abc':
    print 'Cajero autom�tico.'
    print 'a) Ingresar dinero.'
    print 'b) Sacar dinero.'
    print 'c) Consultar saldo.'
    opcion = raw_input('Escoja una opci�n: ')
    if len(opcion) != 1 or opcion not in 'abc':
      print 'S�lo puede escoger las letras a, b o c. Int�ntelo de nuevo.'
  return opcion
