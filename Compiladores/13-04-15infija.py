def esOperador(c):
    if(c=='+'or
       c=='-' or
       c=='/' or
       c=='*'):
        return True
    else:
        return False
def mayorPre(a,b):
    resultado = False
    if ((a=="*")and(b=="+")):
        resultado = True
    if ((a=="+")and(b=="*")):
        resultado = False
    return resultado

infija=['a','*','b','+','c','*','d']
pila=[]

for e in infija:
    if (e=="("):
        pila.append(e)
    elif (e==")"):
        print (e)
    elif (esOperador(e)):
        if(len(pila) == 0 or (mayorPre(e, pila[len(pila)]-1))):
            pila.append(e)
        else:
            a=pila.append(e)
            print (a)
            if (len(pila)==0 or (mayorPre(e, pila[len(pila)-1]))):
                pila.append(e)
    else:
        print (e)
