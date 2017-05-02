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

# Simulación 
while y > 0 and y < altura_paisaje and x > 0 and x < anchura_paisaje - tamanyo_nave:
  vy -= g
  if keypressed(1) == 'Up':
    vy += impulso_y
  elif keypressed(1) == 'Left':
    vx -= impulso_x
  elif keypressed(1) == 'Right':
    vx += impulso_x
  y  += vy
  x += vx
  move(nave, vx, vy)
