a = int(raw_input('Dame el primer n�mero: '))
b = int(raw_input('Dame el segundo n�mero: '))
c = int(raw_input('Dame el tercer n�mero: '))

candidato = a
if b > candidato:
  candidato = b
if c > candidato:
  candidato = c
maximo = candidato

print 'El m�ximo es', maximo
