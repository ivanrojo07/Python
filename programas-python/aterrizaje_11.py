from math import sin, cos, pi
# Paisaje
altura_paisaje = 400 
anchura_paisaje = 400
window_coordinates(0, 0, anchura_paisaje, altura_paisaje)

# Gravedad
g = 0.00001

# Nave
tamanyo_nave = 10
x = anchura_paisaje / 2
y = altura_paisaje - 100
vy = 0
impulso_y = 2*g
impulso_x = 0.00001
vx = 0
nave = create_filled_rectangle(x, y, x+tamanyo_nave, y+tamanyo_nave, 'blue')

# Plataforma
px = anchura_paisaje / 2
py = 0
vpx = .05
anchura_plataforma = 40
altura_plataforma = 3

plataforma = create_rectangle(  px, py, 
  px+anchura_plataforma, py+altura_plataforma, 'red')

# Tanque de combustible
fuel = 1000
consumo = 0.1
create_rectangle(0,altura_paisaje, 10, altura_paisaje-100, 'black')
lleno = create_filled_rectangle(1,altura_paisaje, 9, altura_paisaje-fuel/10, 'green')

# Dial de velocidad
create_circle(anchura_paisaje-50, altura_paisaje-50, 50, 'black')
for i in range(0, 360, 10):
  create_line(  anchura_paisaje-50 + 40 * sin(i*pi/180), \
                altura_paisaje-50 + 40  * cos(i*pi/180), \
                anchura_paisaje-50 + 50 * sin(i*pi/180), \
                altura_paisaje-50 + 50  * cos(i*pi/180))

aguja = create_line(  anchura_paisaje-50, altura_paisaje-50, \
                      anchura_paisaje-50 + 50 * sin(0*pi/180), \
                      altura_paisaje-50 + 50 * cos(0*pi/180), 'blue')

# Simulación 
while y > 0 and y < altura_paisaje and x > 0 and x < anchura_paisaje - tamanyo_nave:
  vy -= g
  if keypressed(1) == 'Up' and fuel > 0:
    vy += impulso_y
    fuel -= consumo
  elif keypressed(1) == 'Left' and fuel > 0:
    vx -= impulso_x
    fuel -= consumo
  elif keypressed(1) == 'Right' and fuel > 0:
    vx += impulso_x
    fuel -= consumo
  y  += vy
  x += vx
  px += vpx 
  if px <= 0 or px >= anchura_paisaje - anchura_plataforma:
    vpx = -vpx
  move(nave, vx, vy)
  move(plataforma, vpx, 0)
  viejo_lleno = lleno 
  lleno = create_filled_rectangle(1,altura_paisaje, 9, altura_paisaje-fuel/10, 'green')
  erase(viejo_lleno) 
  vieja_aguja = aguja
  aguja = create_line(anchura_paisaje-50, altura_paisaje-50, \
                    anchura_paisaje-50 + 50 * sin(1000*vy*pi/180), \
                    altura_paisaje-50 + 50 * cos(1000*vy*pi/180), 'blue')
  erase(vieja_aguja)
