# -*- coding: cp1252 -*-
def imprimeNombre(nombre,apellido,invierte=False):
    if invierte:
        return apellido + " " + nombre
    else:
        return nombre + " " + apellido
print imprimeNombre("Juan","Lopez",True)
print imprimeNombre("Juan","Lopez")
print imprimeNombre(invierte=True, nombre="Juan",apellido="Lopez")
#podemos omitir algun parametro siempre y cuando la variable tenga valor por default
def suma2(n):
    incremento=2
    return n+incremento#es una variable local
print suma2(4)
print suma2(4)*2
print suma2(4)/2
n=7#variable global
incremento=8#variable global
print suma2(n)
#se hara caso primero a la variable local que a la global(encapsulamiento)
a="Jose"
print a[0]
print a[1]
print a[2]
print a[3]
print a[-1]
print a[-2]
print a[-3]
print a[-4]
print a[1:3]
print a[1:2]
print a.find("s")#busca y te da la posición de la primera ocurrencia de variable
b="Maria"
print(b.find("a"))
print (b.find("z"))#si no lo encuentra te marcara -1
print b.count("a")#muestra el numero donde se repite la variable
print a.count("a")
print a.lower()#convierte la cadena en minusculas
print a.upper()#convierte la cadena en mayusculas
c="Esto es una cadena muy larga"
print(c.split())#seprara las palabras o donde haya espacios como arreglos
d="juan,872517,42,6.7"
print (d.split())
print(d.split(","))
e=d.split(",")
print e[0]
print e[3]
f=["gato","perro", "lapiz","pluma","monitor"]
print f
f.sort()#te envia la cadena en orden alfabetico
print f
