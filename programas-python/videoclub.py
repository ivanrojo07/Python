from record import record

class Socio(record):
  dni           = ''
  nombre      = ''
  telefono    = ''
  domicilio   = ''

class Pelicula(record):
  titulo     = ''
  genero     = ''

class Videoclub(record):
  socios      = []
  peliculas   = []

def menu():
  print '*** VIDEOCLUB ***'
  print '1) Dar de alta nuevo socio'
  print '2) Dar de baja un socio'
  print '3) Dar de alta nueva pel�cula'
  print '4) Dar de baja una pel�cula'
  print '5) Salir'
  opcion = int(raw_input('Escoge opci�n: '))
  while opcion < 1 or opcion > 5:
    opcion = int(raw_input('Escoge opci�n (entre 1 y 5): '))
  return opcion

# Programa principal

videoclub = Videoclub()

opcion = menu()
while opcion != 5:

  if opcion == 1:
    print 'Alta de socio'
    socio = lee_socio()
    if contiene_socio_con_dni(videoclub, socio.dni):
      print 'Operaci�n anulada: Ya exist�a un socio con DNI', socio.dni
    else:
      alta_socio(videoclub, socio)
      print 'Socio con DNI', socio.dni, 'dado de alta'

  elif opcion == 2:
    print 'Baja de socio'
    dni = raw_input('DNI: ')    
    if contiene_socio_con_dni(videoclub, dni):
      baja_socio(videoclub, dni)
      print 'Socio con DNI', dni, 'dado de baja'
    else:
      print 'Operaci�n anulada: No existe ning�n socio con DNI', dni

  elif opcion == 3:                                       
    print 'Alta de pel�cula'
    pelicula = lee_pelicula()
    if contiene_pelicula_con_titulo(videoclub, pelicula.titulo):
      print 'Operaci�n anulada: Ya hay una pel�cula con t�tulo', pelicula.titulo
    else:
      alta_pelicula(videoclub, pelicula)
      print 'Pel�cula', pelicula.titulo, 'dada de alta'

  elif opcion == 4:
    print 'Baja de pel�cula'                        
    titulo = raw_input('T�tulo: ')     
    if contiene_pelicula_con_titulo(videoclub, titulo):
      baja_pelicula(videoclub, titulo)
      print 'Pel�cula', titulo, 'dada de baja'
    else:
      print 'Operaci�n_anulada: No existe ninguna pel�cula llamada', titulo

  opcion = menu()

print 'Gracias por usar nuestro programa'
