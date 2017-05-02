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

nave = create_filled_rectangle(x, y, x+tamanyo_nave, y+tamanyo_nave, 'blue')

# Simulación 
while y > 0  and y < altura_paisaje:
  vy -= g
  if keypressed(1) == 'Up':
    vy += impulso_y
  y  += vy
  move(nave, 0, vy)
