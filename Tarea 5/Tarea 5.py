# -*- coding: cp1252 -*-
#Rojo Orea Guillermo Iv�n
#cargaPalabras("words.txt") o escribir la direcci�n del directorio

def cargaPalabras(NombredelDocumento):
    palabras=[]
    lectura = open(NombredelDocumento)
    lines=lectura.read().splitlines()
    for i in range(len(lines)):
        data = lines[i]
        data = data.split()
        palabras=(data)
    return len(palabras)
    lectura.close
print (cargaPalabras("words.txt"))
