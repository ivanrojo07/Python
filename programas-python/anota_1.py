nota = raw_input('Nota a a�adir: ')
f = open('notas.txt', 'a')
f.write(nota + '\n')
f.close()  
