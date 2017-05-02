    
archivo = open("Alumnos.db")
linea=archivo.read().splitlines()
nom=[]
cuen=[]
grup=[]
asist=[]
calif=[]

for i in range(len(linea)):
    datos = linea[i]
    datos = datos.split(',')
    nom.append(datos[0])
    cuen.append(datos[1])
    grup.append(datos[2])

    if datos[3] == "True":
        asist.append(True)
    else:
        asist.append(False)
        
    calif.append(float(datos[4]))

    alumno=(nom,cuen,grup,asist,calif)


print ("Aprobados: ")
for i in range(len(calif)):
    
    if (calif[i] > 5.99) and (alumno[3][i]) == True:
        print "Nombre: ",(alumno[0][i]),"\n","Calificación:",(alumno[4][i]),"\n"

print "Reprobados: "
for i in range(len(calif)):
    
    if (calif[i] < 6) or (alumno[3][i]) == False:
        if (alumno[3][i]) == False:
            print "Nombre: ",(alumno[0][i]),"NP","\n","Calificación:",(alumno[4][i]),"\n"
        else:
            print "Nombre: ",(alumno[0][i]),"\n","Calificación:",(alumno[4][i]),"\n"
        
archivo.close
