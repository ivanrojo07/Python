def menu():
  opcion = ''
  while not ('a' <= opcion <= 'c'):
    print 'Cajero autom�tico.'
    print 'a) Ingresar dinero.'
    print 'b) Sacar dinero.'
    print 'c) Consultar saldo.'
    opcion = raw_input('Escoja una opci�n: ')
    if not (opcion >= 'a' and opcion <= 'c'):
      print 'S�lo puede escoger las letras a, b o c. Int�ntelo de nuevo.'
  return opcion
