import re
archivo = open("c++.txt","r")
texto=archivo.read()
print re.sub(r'/*.*/', " ", texto)#el . significa cualquier caracter menos el de la linea
print (texto)

archivo.close()
