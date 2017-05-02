#Clase 01 Manejo de archivos 2
archivo= open ("c++.txt", "r")
texto = archivo.read()
texto2=texto.split()

print(texto)
print (texto2)
archivo.close()
