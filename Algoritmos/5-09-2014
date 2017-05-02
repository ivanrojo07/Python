# -*- coding: cp1252 -*-
#Manejo de archivos
archivo = open('lista.txt','w')#Crear archivo llamado lista.txt
#w: abre el archivo para escritura
#r: abre el archivo para lectura
#a: abre el archivo para escribir al final de él
archivo.write('Iván\n')
archivo.writelines('Rojo')
archivo.close()

#agrega caracteres al archivo
archivo1 = open('Agregar.txt','a')

for cont in range(3):
    nom = raw_input("Nombre: ")
    archivo1.write(nom)
    
archivo.close()

#lee el archivo
lectura = open ('lista.txt', 'r')
for linea in lectura:
    print linea


#Tuplas
""">>> a=(1,2,3)
>>> a[0]
1
>>> a[2]
3
>>> b=(´hola´,7, 3.25,True)
SyntaxError: invalid syntax
>>> b=('hola',7, 3.25,True)
>>> b[0]
'hola'
>>> b[1]
7
>>> b[2]
3.25
b[3]
True
>>> c=('ivan','rojo')
>>> d=(a,b,c)
>>> d
((1, 2, 3), ('hola', 7, 3.25, True), ('ivan', 'rojo'))
>>> d[0]
(1, 2, 3)
>>> c[1]
'rojo'
>>> d[2][1]
'rojo'"""


