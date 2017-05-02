#Rojo Orea Guillermo Iván Grupo: 1508
print "Programa 1"
lista= [0,0,0,0,0,0,0,0,0,0]
i=0

while i < 10:
    num=int(raw_input("Numero: "))
    lista[i]=num
    i=i+1
print lista

j = 0
impar = 1
while j < len(lista):
    if (lista[j] % 2) == 1:
        if lista[j] > impar:
            impar = lista[j]
    j = j + 1
    

if impar != 1:
    print ("El impar mayor es: ",impar)
else:
    print ("Solo pares")

#Rojo Orea Guillermo Iván Grupo:1508
print "Programa 2"
x=str(raw_input("Escribe tu nombre: "))
caracter = ''
for cont in x:
  caracter = cont + caracter
print caracter
