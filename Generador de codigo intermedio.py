def esOperador(c):
    if(c=='+'or
       c=='-' or
       c=='/' or
       c=='*'):
        return True
    else:
        return False

       
fpos="ab*cd*+"
pila=[]
for c in fpos:
    print c
    if fpos[c]== esOperador(c):
        print pila:
    e
