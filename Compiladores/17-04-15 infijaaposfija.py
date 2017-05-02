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
def infija(entrada):
    error=False
    pila =[]
    pilaTemp=[]

    salida=[]

    for e in entrada:
        if (e=="("):
            pila.append(e)
        elif (e==")"):
            print (e)
        elif (esOperador(e)):
            while ((len(pila)!=0)and (mayorPre(pila[len(pila)-1],e))):
                salida.append(pila.pop())
            pila.append(e)
        else:
            salida.append(e)
    while(len(pila)!=0):
        salida.append(pila.pop())
    return salida
