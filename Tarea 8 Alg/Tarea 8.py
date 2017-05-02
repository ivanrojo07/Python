#Rojo Orea Guillermo Iván
# -*- coding: cp1252 -*-

def ContadorLetras(cadena):
    total= 0
    alfabeto = "abcdefghijklmnñopqrstuvwxyz"

    for letra in cadena:
        if letra in alfabeto:
            total= total+1

    for letra in alfabeto:
        if letra in cadena:
            print letra,cadena.count(letra),(float(cadena.count(letra))/(total))*100, '%'
            
            
        else:
            print letra,cadena.count(letra), '0', '%'
    
   
def cargaOriginal(nombre):
    archivo = open(nombre, 'r')
    renglon = archivo.read()
    archivo.close()
    return renglon

archivo1 = cargaOriginal('fundacion.txt')
print "Fundación"
ContadorLetras(archivo1)

print '\n'

print "La Muerte de Artemio Cruz"
archivo2 =cargaOriginal('laMuertedeArtemioCruz.txt')
ContadorLetras(archivo2)
