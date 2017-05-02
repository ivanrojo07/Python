#Rojo Orea Guillermo Iván 
# -*- coding: cp1252 -*-
import re
archivo = open("c++.txt","r")
texto = archivo.read()
print texto

sc = re.sub(r"/*.*/"," ",texto)
texto2 = sc.split()

var="abcdefghijklmnñopqrstuvwxyzABCDEFGHIJKLMNÑOPQRSTUVWXYZ0123456789"
simb = "!#%&/()='+-*^[]{},;.:<>"
num="1234567890"
palreserv=['#include', '<stdio.h>','public', 'class', 'static', 'void', 'main', 'String', 'args','int', 'IntegerparseInt', 'null']
palabra=[]
simbolo=[]

while len(texto2)>0:
    selec= ''
    b=texto2[0]

    for i in range(len(b)):
        if b[i] in var:
            selec = selec + b[i]
        else:
            simbolo.append(b[i])

    if selec != '':
        palabra.append(selec)

    for j in range(len(simbolo)):
        palabra.append(simbolo[0])
        simbolo.remove(simbolo[0])
    
    texto2.remove(b)


for i in range(len(palabra)):
    c=''
    a = len(palabra[i])
    a= 30-a
    for j in range(a):
        c= '' + c
    if palabra[i] in simb or palabra[i] == '"':
        print palabra[i],c,': Es simbolo.'
    elif palabra[i] in num:
        print palabra[i],c,': Es dato.'
    elif palabra[i] in palreserv:
        print palabra[i],c,': Es palabra reservada.'
    else:
        print palabra[i],c,': Es identificador.'

print 'Usted tiene: ', len(palabra),' token(s)'

archivo.close()
