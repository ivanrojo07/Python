from math import sin, cos, pi

x = 500
y = 500
radio = 500
suspensos = 10
aprobados = 20
notables = 40
sobresalientes = 30

create_circle(x, y, radio)
create_line(x, y, x+radio, y)

alfa = 2*pi*suspensos/100
create_line(x, y, x+radio*cos(alfa), y+radio*sin(alfa))
create_text(x+.5*radio*cos(alfa/2), y+.5*radio*sin(alfa/2),'sus (%d%%)' % suspensos)

beta = 2*pi*(suspensos+aprobados)/100
create_line(x, y, x+radio*cos(beta), y+radio*sin(beta))
