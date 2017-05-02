# -*- coding: cp1252 -*-
#25 de marzo 2015 listas
a=[1,2,3,4,5]
print a
b="Te hace falta ver mas baaax"
for e in a:
    print (e)

print b.split()
print b[5:12]
print b[5:]
print b[:5]

a.pop()
print a

a.append( 8 );
print a

def esOperador(c):
    return(c in "*+-/")
    
pila=[]
posfija = "ab*cd*+"
t=0
for e in posfija:
    if esOperador(e):
        op2=pila.pop()
        op1=pila.pop()
        print ("t"+str(t)+":="+op1+e+op2+";")
        pila.append("t"+str(t))
        t=t+1
    else:
        pila.append(e)

c="t1:=c*d;"
pi=c.find("=")
pf=c.find("*")
print pi
print pf
print c[pi+1:pf]
print ("LDA "+c[pi+1:pf]+";")

