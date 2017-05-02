#Clase 01 Manejo de archivos
archivo= open ("uno.txt", "r")
texto = archivo.read()
texto2=texto.split()

print(texto)
print (texto2)
archivo.close()
