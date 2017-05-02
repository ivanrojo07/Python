
palabras=[]
lectura = open("words.txt")
lines=lectura.read().splitlines()
for i in range(len(lines)):
    data = lines[i]
    data = data.split()
    palabras=(data)
print len(palabras)
lectura.close
cont =0

frase = 'zxoxiosvx zxu nhllyxa: gdrey txsypn gevx zaxern. xvxy zlpn gevx zaxern, tdo ylo bld, bld eax jdno e reigsyx. ey srsoeosly lm usmx. iey e altlo wasox e nbrhglyb? iey e altlo oday e... ieyven syol e txedosmdu renoxahsxix?  -nlyyb: iey bld?'
print len(frase)

for pal in palabras:
    if len(pal) ==3 and pal[0]=='a' and pal[2]=='e':
        print pal
        cont = cont +1
print cont

def ContadorLetras(cadena):
    total= 0
    alfabeto = "abcdefghijklmnñopqrstuvwxyz"

    for letra in cadena:
        if letra in alfabeto:
            total= total+1

    for letra in alfabeto:
        if letra in cadena:
            print letra,cadena.count(letra),(float(cadena.count(letra))/(total))*100, '%'
            
            
        else:
            print letra,cadena.count(letra), '0', '%'
ContadorLetras(frase)
for pal in palabras:
    if len(pal) ==3 and pal[1]=='a' and pal[1]=='a':
        print pal
cont =0
for pal in palabras:
    if len (pal)==5 and pal[1]== pal[3] and pal[1]!= 'a' and pal[1]!='e':
        print pal
cont = cont +1
print cont
for pal in palabras:
    if len (pal)==4 and pal[0]== pal[2] and pal[0]!= 'a':
        print pal
