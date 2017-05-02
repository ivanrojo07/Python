#Rojo Orea Guillermo Iván
def cifradoCesarTexto(cadena,num, alfabetom):
    nuevaCadena = ""
    for i in range(len(cadena)):
        if (alfabetom.find(cadena[i]) != -1):
            indice = alfabetom.find(cadena[i]) + num
            while indice < 0 or indice >= len(alfabetom):
                if indice > len(alfabetom) - 1:
                    indice = indice - len(alfabetom)
                elif indice < 0:
                    indice = indice + len(alfabetom)
            nuevaCadena += alfabetom[indice]
        else:
            nuevaCadena += cadena[i]
    return nuevaCadena

def anular(prueba, alfabetom):
    palabra = ""
    for b in range(len(prueba)):
        if (alfabetom.find(prueba[b]) != -1):
            palabra += prueba[b]
    return palabra

def cifradoCesar(cadena, num):
    nuevaCadena = ""
    alfabeto = 'abcdefghijklmnopqrstuvwxyz'
    for i in range(len(cadena)):
        indice = alfabeto.find(cadena[i]) + num
        if not(cadena[i] in alfabeto):
            nuevaCadena += cadena[i]
        else:
            while indice < 0 or indice >= 25:
                if indice > 25:
                    indice = indice - 26
                elif indice < 0:
                    indice = indice + 26
            nuevaCadena += alfabeto[indice]
    return nuevaCadena


alfabeto = 'abcdefghijklmnopqrstuvwxyz'
texto = open("textoCifrado.txt", "r")
dicc = open("words.txt", "r")
palabras = dicc.read().split()
final = texto.read()
texCif = final.lower().split()
texto.close()
dicc.close()
indice = []
lista = []

for a in range(len(texCif)):
    lista.append(anular(texCif[a], alfabeto))


for i in range(len(alfabeto)):
    contador = 0
    print 'Posibilidad:',i
    for j in range(len(lista)):
        posible = cifradoCesarTexto(lista[j], i, alfabeto)
        for k in range(len(palabras)):
            if (posible == palabras[k]):
                print 'Coincidencia en:',posible
                contador += 1
    indice.append(contador)


mayor = 0
apuntador = 0
for numero in range(len(indice)):
    if indice[numero] > mayor:
        mayor = indice[numero]
        apuntador = numero

print 'La llave que más sentido tiene es la:',apuntador, 'con',mayor,'coincidencia'
print 'La cadena es:'
print cifradoCesar(final, apuntador - len(alfabeto))
