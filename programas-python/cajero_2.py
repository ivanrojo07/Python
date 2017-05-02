carga50 = 100
carga20 = 100
carga10 = 100

def sacar_dinero(cantidad):
  global carga50, carga20, carga10
  de50 = cantidad / 50
  cantidad = cantidad % 50
  de20 = cantidad / 20
  cantidad = cantidad % 20
  de10 = cantidad / 10
  carga50 = carga50 - de50
  carga20 = carga20 - de20
  carga10 = carga10 - de10
  return [de50, de20, de10]

c = int(raw_input('Cantidad a extraer: '))
print sacar_dinero(c)
