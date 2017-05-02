from record import record

# Tipo Entrada
class Entrada(record):
  nombre     = ''
  apellido   = ''
  telefono   = ''

def lee_entrada():
  nombre = raw_input('Nombre: ')
  apellido = raw_input('Apellido: ')
  telefono = raw_input('Teléfono: ')
  return Entrada(nombre=nombre, apellido=apellido, telefono=telefono)

# Tipo Agenda
class Agenda(record):
  lista = []

def cargar_agenda(agenda):
  agenda.lista = []
  f = open('agenda.txt', 'r')
  while 1:
    linea1 = f.readline()
    linea2 = f.readline()
    linea3 = f.readline()
    if linea1 == '':
      break
    entrada = Entrada(nombre=linea1[:-1], apellido=linea2[:-1], telefono=linea3[:-1])
    agenda.lista.append(entrada)
  f.close()

def guardar_agenda(agenda):
  f = open('agenda.txt', 'w')
  for entrada in agenda.lista:
    f.write(entrada.nombre + '\n')
    f.write(entrada.apellido + '\n')
    f.write(entrada.telefono + '\n')
  f.close()

# Estas tres funciones no trabajan directamente con el fichero, sino con los datos
# almacenados previamente en memoria.
def buscar_telefono(agenda, nombre, apellido):
  for entrada in agenda.lista:
    if entrada.nombre == nombre and entrada.apellido == apellido:
      return entrada.telefono
  return ''

def anyadir_entrada(agenda, entrada):
  agenda.lista.append(entrada)

def borrar_entrada(agenda, nombre, apellido):
  for i in range(len(agenda.lista)):
    if agenda.lista[i].nombre == nombre and agenda.lista[i].apellido == apellido:
      del agenda.lista[i]
      return

# Menú de usuario
def menu():
  print '1) Añadir entrada'
  print '2) Consultar agenda'
  print '3) Borrar entrada'
  print '4) Salir'
  opcion = int(raw_input('Seleccione opción: '))
  while opcion < 1 or opcion > 4:
    opcion = int(raw_input('Seleccione opción (entre 1 y 4): '))
  return opcion
    

# Programa principal
agenda = Agenda()
cargar_agenda(agenda)

opcion = menu()
while opcion != 4:
  if opcion == 1:
    entrada = lee_entrada()
    anyadir_entrada(agenda, entrada)
  elif opcion == 2:
    nombre = raw_input('Nombre')
    apellido = raw_input('Apellido: ')
    telefono = buscar_telefono(agenda, nombre, apellido)
    if telefono == '':
      print 'No está en la agenda'
    else:
      print 'Teléfono:', telefono
  elif opcion == 3:
    nombre = raw_input('Nombre: ')
    apellido = raw_input('Apellido: ')
    borrar_entrada(agenda, nombre, apellido)
  opcion = menu()

guardar_agenda(agenda)
