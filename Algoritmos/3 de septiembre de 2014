def fibo(x):
    "assumes x an int >=0 Return Fibonacci of x"
    global numcalls
    numcalls +=1 #numcals= numcalls + 1
    if x==0 or x==1:
        return 1
    else:
        return fibo(x-1)+fibo(x-2)
def testfib(n):
    for i in range (n+1):
        global numcalls
        numcalls=0
        print "fibonacci de ", i, '=',fibo(i)
        print "Fibonacci llamado", numcalls, 'veces'
a= 'hola'
len (a)
#4
a[0]
#'h'
a[0:len (a)]
#'hola'
#[0:len(a)]
#SyntaxError: invalid syntax
#a[len(a)]

#Traceback (most recent call last):
#  File "<pyshell#9>", line 1, in <module>
#    a[len(a)]
#IndexError: string index out of range
b= "casa"
c= "grande"
d= b+c
print d

def invierteCad(cadena):
    if len(cadena)==1:
        return cadena
    else:
        return cadena[-1]+invierteCad(cadena[0:len(cadena)-1])
