cont=0
raiz=int(raw_input("Escribe el valor de x: "))
posibleraiz=raiz-(cont*cont)#margen de error (de 0.1)
while posibleraiz >=0.1:
    cont= cont+0.1
    print("probando la posible raiz",cont)
    posibleraiz=raiz-(cont*cont)
    print("El error actual es: ", posibleraiz)
print ("la raiz del numero es ",cont)

#if condicion:
    #.......
#elif condicion:
    #.........
#elif condicion:
    #.........
#else:
    #.........
d="abcde"
d
len(d)
