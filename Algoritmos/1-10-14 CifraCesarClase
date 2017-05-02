def cifraCesar(cadena,llave):
    if llave < 0:
        llave = 26 - llave
    cadena = cadena.lower()
    nuevaCadena=""
    alfabeto='abcdefghijklmnopqrstuvwxyz'
    for l in cadena:
        if l in alfabeto:
            posicionLetra=alfabeto.find(l)
            nuevaCadena=nuevaCadena + alfabeto[(posicionLetra + llave)%26]
        else:
            nuevaCadena=nuevaCadena + l
    return nuevaCadena
def getAciertos(listaPalabras, diccionario):
    numAciertos=0
    for pal in listaPalabras:
        if pal in diccionario:
            numAciertos=numAciertos + 1
    return numAciertos
palabras = cargaPalabras()
cadena = cargaCifrado()
maxAciertos=0
posibleLlave=0

def cargaPalabras():
    archivo=open('word.txt','r')
    renglo=archivo.redline()
    palabras=renglon.split()
    print len(palabras), "palabras leidas"
    return palabras 

for cont in range(26):
    cadenaCifrada = cifraCesar(Cadena,cont)
    listaCifrada = cadenaCifrada.split()
    numAciertos = getAciertos(listaCifrada,palabras)
    if numAciertos > maxAciertos:
        posibleLLave = cont
print 'La llave es ', posibleLlave
print "El texto descifrado es:"
print (cifradoCesar(cadena,posibleLlave))

#import random
#random.randint(1,100)
