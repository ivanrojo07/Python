from smtplib import SMTP

servidor = SMTP('alu-mail.uji.es')
remitente = 'al00000@alumail.uji.es'
texto = 'Estimado =S =A:\n\n'
texto += 'Por la presente le informamos de que nos debe usted la '
texto += 'cantidad de =E euros. Si no abona dicha cantidad antes '
texto += 'de 3 d�as, su nombre pasar� a nuestra lista de morosos.'

seguir = 's'
while seguir == 's':
  destinatario = raw_input('Direcci�n del destinatario: ')
  tratamiento  = raw_input('Tratamiento: ')
  apellido     = raw_input('Apellido: ')
  euros        = raw_input('Deuda (en euros): ')

  mensaje = 'From: %s\nTo: %s\n\n' % (remitente, destinatario)

  personalizado = ''
  i = 0
  while i < len(texto):
    if texto[i] != '=':
      personalizado += texto[i]
    else:
      if texto[i+1] == 'A':
        personalizado += apellido
        i = i + 1
      elif texto[i+1] == 'E':
        personalizado += euros
        i = i + 1
      elif texto[i+1] == 'S':
        personalizado += tratamiento
        i = i + 1
      else:
        personalizado += '='
    i = i + 1
  mensaje += personalizado

  servidor.sendmail(remitente, destinatario, mensaje)
  seguir = raw_input('Si desea enviar otro correo, pulse \'s\': ')
