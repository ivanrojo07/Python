def menu():
  opcion = ''
  while not ('a' <= opcion <= 'c'):
    print 'Cajero automático.'
    print 'a) Ingresar dinero.'
    print 'b) Sacar dinero.'
    print 'c) Consultar saldo.'
    opcion = raw_input('Escoja una opción: ')
    if not (opcion >= 'a' and opcion <= 'c'):
      print 'Sólo puede escoger las letras a, b o c. Inténtelo de nuevo.'
  return opcion
