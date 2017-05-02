# -*- coding: cp1252 -*-
#Rojo Orea Guillermo Iván
abc = 'abcdefghijklmnopqrstuvwxyz'
def cifradoCesar(cadena, llave):
 
	textocifrado = ''
 
	for letra in cadena:
		suma = abc.find(letra) + llave
		modulo = int(suma) % len(abc)
		textocifrado = textocifrado + str(abc[modulo])
		espacio= ' '
 
	return textocifrado

cadena = str(raw_input('cadena a cifrar: ')).lower()
llave= int(raw_input('llave numerica: '))
print cifradoCesar(cadena,llave)

