# -*- coding: cp1252 -*-
import random
a="abcdefghijklmnopqrstuvwxyz"
pos=int(raw_input("¿Qué letra quieres quitar?"))
b= a[0:pos]+a[pos+1:len(a)]
print(b)

alfabeto=str(raw_input("Muestre su alfabeto: "))
nuevoAlfabeto=""
posicionesUtilizadas=[]
while len(posicionesUtilizadas)<len(alfabeto):
    aleatorio=random.randint(0,len(alfabeto)-1)
    if not aleatorio in posicionesUtilizadas:
        posicionesUtilizadas.append(aleatorio)
        nuevoAlfabeto+=alfabeto[aleatorio]
print nuevoAlfabeto
