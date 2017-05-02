import random
def creaDicAleatorio(alfabeto):
    nuevoAlfabeto=""
    while len (alfabeto)>0:
        pos= random.randint(0,len(alfabeto)-1)
        nuevoAlfabeto=nuevoAlfabeto +alfabeto[pos]
        alfabeto= alfabeto[0:pos]+alfabeto[pos +1:len (alfabeto)]
    return nuevoAlfabeto
alfabeto='abcdefghijklmnopqrstuvwxyz'
print (creaDicAleatorio(alfabeto))

def cifraSustituye(cadena,alfabetollave):
    alfabeto='abcdefghijklmnopqrstuvwxyz'
    cadena=cadena.lower()
    nuevaCadena=""
    for l in cadena:
        if (l in alfabeto):
            nuevaCadena= nuevaCadena + alfabetollave[alfabeto.find(l)]
        else:
            nuevaCadena= nuevaCadena + l
    return nuevaCadena
miAlfabeto = 'hvzixtjkuldgmwcfbynpqraeso'
e=cifraSustituye("Ola",miAlfabeto)
print e

def cifraDecifra(cadena,alfabetollave):
    alfabeto='abcdefghijklmnopqrstuvwxyz'
    cadena=cadena.lower()
    nuevaCadena=""
    for l in cadena:
        if (l in alfabeto):
            nuevaCadena= nuevaCadena + alfabeto[alfabetollave.find(l)]
        else:
            nuevaCadena= nuevaCadena + l
    return nuevaCadena

print cifraDecifra(e,miAlfabeto)

f="ts yof rt ltdqfq ekolzoqf lt hxlg wotf ugkrg egdotfrg qsozql n eglozossql"
print f.count("k")
