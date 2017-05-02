from math import sqrt

window_coordinates(-500, -500, 500, 500)

x1 = -200
y1 = -200
velocidad_x1 = 0.1
velocidad_y1 = 0
m1 = 20

x2 = 200
y2 = 200
velocidad_x2 = -0.1
velocidad_y2 = 0
m2 = 20

circulo_1 = create_circle(x1, y1, m1, 'red')
circulo_2 = create_circle(x2, y2, m2, 'blue')

for t in range(10000):
  
  r3 = sqrt( (x2-x1)**2 + (y2-y1)**2 ) ** 3
  
  aceleracion_x1 = m2 * (x2 - x1) / r3
  aceleracion_y1 = m2 * (y2 - y1) / r3
  aceleracion_x2 = m1 * (x1 - x2) / r3
  aceleracion_y2 = m1 * (y1 - y2) / r3

  velocidad_x1 += aceleracion_x1
  velocidad_y1 += aceleracion_y1
  velocidad_x2 += aceleracion_x2
  velocidad_y2 += aceleracion_y2

  viejo_x1 = x1
  viejo_y1 = y1
  viejo_x2 = x2
  viejo_y2 = y2

  x1 += velocidad_x1
  y1 += velocidad_y1
  x2 += velocidad_x2 
  y2 += velocidad_y2

  move(circulo_1, velocidad_x1, velocidad_y1)
  create_line(viejo_x1, viejo_y1, x1, y1, 'red')
  move(circulo_2, velocidad_x2, velocidad_y2)
  create_line(viejo_x2, viejo_y2, x2, y2, 'blue')
