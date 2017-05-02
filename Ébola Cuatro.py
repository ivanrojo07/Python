# -*- coding: cp1252 -*-
from Tkinter import *
from time import sleep
from math import *
from random import *

def distancia(x1, y1, x2, y2):
    return sqrt( pow( (x2 - x1), 2) + pow( (y2 - y1), 2) )

class Persona():
    def __init__(self, c):
        self.numero = c
        self.sano = True
        self.inmune = False
        self.vacunado = False
        self.contactos = []
        self.sanoDesde = 0
        self.posicionX = 0
        self.posicionY = 0
        self.infecciosidad = 0

def creaPoblacion():
    poblacion = []
    for c in range(1600):
        poblacion.append(Persona(c))
    return poblacion

def dibujaPoblacion(poblacion):
    
    for c in range(len(poblacion)):
        x = c % 40
        y = c / 40
        poblacion[c].posicionX = x
        poblacion[c].posicionY = y
        if poblacion[c].sano:
            lienzo.create_oval(x * 10, y * 10, x*10 + 11, y*10 + 11, fill = "blue")
        if poblacion[c].inmune:
            lienzo.create_oval(x * 10, y * 10, x*10 + 11, y*10 + 11, fill = "green")
        if poblacion[c].vacunado:
            lienzo.create_oval(x * 10, y * 10, x*10 + 11, y*10 + 11, fill = "yellow")
        elif not poblacion[c].sano:
            lienzo.create_oval(x * 10, y * 10, x*10 + 11, y*10 + 11, fill = "red")
    #sleep(0.5)

def correSim():
    print 'Aquí va el código de la simulación'
    dibujaPoblacion(poblacion)
    # Parte donde se asignan los contactos más cercanos.
    for a in range(len(poblacion)):
        for b in range(len(poblacion)):
            d = distancia(poblacion[a].posicionX, poblacion[a].posicionY, poblacion[b].posicionX, poblacion[b].posicionY)
            if  d < 1.5 and not(int(d) == 0):
                poblacion[a].contactos.append(poblacion[b].numero)
    aleatorio = 0
    
    # Parte donde se hacen los contactos aleatorios.
    for c in range(len(poblacion)):
        while len(poblacion[c].contactos) < 10:
            aleatorio = randint(0, len(poblacion) - 1)
            if not (aleatorio in poblacion[c].contactos):
                poblacion[c].contactos.append(aleatorio)
        poblacion[c].contactos.sort()
    aleatorio = randint(0, len(poblacion) - 1)

    # Se hace al primer infectado.
    poblacion[aleatorio].sano = False
    poblacion[aleatorio].infecciosidad = randint(1, 50)
    print 'El primer habitante infectado es el número', aleatorio
    dibujaPoblacion(poblacion)

    # Parte donde se hace la simulación por días.
    numeroInfectivo = 0
    infeccionPoblacion = 0
    habitante = 0
    vacuna = 0
    poblacionInfectada = []
    poblacionInfectada.append(aleatorio)
    
    for i in range(20): # Aquí debe ir el número de días de la simulación.
        print 'Día', i + 1, 'de 20.'
        sleep(0.5)
        ventana.update()
        dibujaPoblacion(poblacion)
        for k in range(50):
            vacuna = randint(0, len(poblacion) - 1)
            if poblacion[vacuna].sano:
                poblacion[vacuna].vacunado = True
        for j in range(len(poblacion)):
            numeroInfectivo = randint(0, 100)
            #for k in range(len(poblacion[j].contactos)):
                #if poblacion[k].sano == False:
                    #poblacion[j].contactos.remove(poblacion[k].numero)
            if poblacion[j].sano == False and numeroInfectivo < poblacion[j].infecciosidad:# and not (poblacion[j].contactos in poblacionInfectada):
                for k in range(len(poblacion[j].contactos)):
                    if not (poblacion[j].contactos[k] in poblacionInfectada):
                        infeccionPoblacion = randint(0, len(poblacion[j].contactos) - 1)
                        habitante = poblacion[j].contactos[infeccionPoblacion]
                        poblacion[habitante].sano = False
                        poblacion[habitante].infecciosidad = randint(1, 100)
                        poblacionInfectada.append(habitante)
            
                #print 'El habitante', poblacion[j].numero, 'infectó al habitante', habitante
        dibujaPoblacion(poblacion)
        print 'Fin de la simulación.'

#Sección de la lógica del programa.
poblacion =  creaPoblacion()

# Sección de la interfaz gráfica.
ventana = Tk()
lienzo = Canvas(ventana, width = 404, height = 404)
lienzo.pack()
botonSalir = Button(ventana, text = "Salir", fg = "black", command = ventana.quit)
botonSalir.pack(side = LEFT)
boton1 = Button(ventana, text = "Corre simulación", command = correSim)# state = DISABLED)
boton1.pack(side = LEFT)
#etiquetaN = Text(ventana, selectborderwidth = 40)
#nDias = etiquetaN.
#etiquetaN.pack(side = LEFT)
mainloop()
ventana.destroy()
