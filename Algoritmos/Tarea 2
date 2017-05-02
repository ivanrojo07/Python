# -*- coding: cp1252 -*-
archivo= open('Alumnos.db','w')
tupla= [0,0,0,0,0]
i = 0
while i<5:
    nom=str(raw_input('Agregar nombre: '))
    archivo.write(nom + ',')
    cuen=str(raw_input('Agrega numero de cuenta: '))
    archivo.write(cuen + ',')
    grup=str(raw_input('Agrega el Grupo: '))
    archivo.write(grup + ',')
    asist=raw_input('Cumple asistencia: ')
    archivo.write(asist + ',')
    calif=str(raw_input('Calificación: '))
    archivo.write(calif)
    archivo.write('\n')
    alumno=(nom,cuen,grup,asist,calif)
    tupla[i]= alumno
    i= i+1
archivo.close()
