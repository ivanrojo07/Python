def min(a, b):
  if a < b:
    return a
  else:
    return b

def max(a, b):
  if a > b:
    return a
  else:
    return b

if __name__ == '__main__':
  print 'El m�ximo de 3 y 10 es',  max(3,10)
  print 'El m�ximo de 3 y -10 es', max(3,-10)
  print 'El m�nimo de 3 y 10 es',  min(3,10)
  print 'El m�nimo de 3 y -10 es', min(3,-10)
