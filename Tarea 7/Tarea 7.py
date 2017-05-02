# -*- coding: cp1252 -*-
import random

#1.-Escriba la función que dada una cadena y un alfabeto llave, devuelva la cadena cifrada

def cifraSustituye(cadena, alfabetoLlave):
    nuevaCadena = ""
    cadena = cadena.lower()
    alfabeto = 'abcdefghijklmnopqrstuvwxyz'
    for i in range(len(cadena)):
        if (alfabeto.find(cadena[i]) != -1):
            indice = alfabeto.find(cadena[i])
            nuevaCadena += alfabetoLlave[indice]
        else:
            nuevaCadena +=cadena[i]
    return nuevaCadena
miAlfabeto = 'hvzixtjkuldgmwcfbynpqraeso'
cadenaCifrada = cifraSustituye("casa", miAlfabeto)
print "Cadena cifrada: ",cadenaCifrada

#2.- Escriba la función que dada la cadena cifrada y el alfabeto llave devuelva la cadena original.

def descifraSustituye(cadena, alfabetoLlave):
    nuevaCadena=""
    cadena=cadena.lower()
    alfabeto='abcdefghijklmnopqrstuvwxyz'
    for i in range(len(cadena)):
        if (alfabeto.find(cadena[i]) != -1):
            indice = alfabetoLlave.find(cadena[i])
            nuevaCadena += alfabeto[indice]
        else:
            nuevaCadena +=cadena[i]
    return nuevaCadena

miAlfabeto = 'hvzixtjkuldgmwcfbynpqraeso'
cadenaCifrada = cifraSustituye("casa", miAlfabeto)
cadenaDescifrada = descifraSustituye(cadenaCifrada, miAlfabeto)
print "cadena descifrada: ", cadenaDescifrada

#3.- Escriba un algoritmo que dado un alfabeto cree otro en orden aleatorio

def creaDiccAleatorio(alfabeto):
    nuevoAlfabeto=""
    posicionesUtilizadas=[]
    while len(posicionesUtilizadas)<len(alfabeto):
        aleatorio=random.randint(0,len(alfabeto)-1)
        if not aleatorio in posicionesUtilizadas:
            posicionesUtilizadas.append(aleatorio)
            nuevoAlfabeto+=alfabeto[aleatorio]
    return nuevoAlfabeto
alfabeto = 'abcdefghijklmnopqrstuvwxyz'
print "Diccionario aleatorio: ",creaDiccAleatorio(alfabeto), "\n"

#4.- Haga un pequeño programa que lea un archivo lo cifre utilizando la llave:

miAlfabeto='hvzixtjkuldgmwcfbynpqraeso'

#lo descifre e imprima el texto original, el texto cifrado y el texto descifrado
#(deben ser muy parecidos, salvo que las mayúsculas se convierten en minúsculas).

def cargaOriginal():
    archivo = open('textoprueba.txt', 'r')
    renglon = archivo.readline()
    archivo.close()
    return renglon


print "Texto Original: ", cargaOriginal(), "\n"

cadenaCifrada = cifraSustituye(cargaOriginal(), miAlfabeto)
print "Texto Cifrado: ",cadenaCifrada, "\n"

print "Texto Descifrado: ", descifraSustituye(cadenaCifrada, miAlfabeto)

