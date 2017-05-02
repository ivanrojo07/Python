# -*- coding: cp1252 -*-
from Tkinter import *
from time import sleep
from math import*

def distancia(x1,y1,x2,y2):
    return math.sqrt(pow((x2-x1),2)+pow((y2-y1),2))

class Persona():
    def __init__(self,c):
        self.sano = True
        self.inmune= False
        self.vacunado=False
    ## agregar lo que corresponda.

def creaPoblacion():
    poblacion = []
    for c in range(1600):
        poblacion.append(Persona(c))
    return poblacion

def dibujaPoblacion(poblacion):
    for c in range(1600):
        x =c%40
        y =c/40
        if poblacion[c].sano:
            lienzo.create_oval(x*10, y*10, x*10+11, y*10+11, fill = "blue")
        if poblacion[c].inmune:
            lienzo.create_oval(x*10, y*10, x*10+11, y*10+11, fill = "green")
        if poblacion[c].vacunado:
            lienzo.create_oval(x*10, y*10, x*10+11, y*10+11, fill = "yellow")
        elif not poblacion[c].sano:
            lienzo.create_oval(x*10, y*10, x*10+11, y*10+11, fill = "red")
        
    

def correSim():
    print 'Aqu� va el c�digo de la simulaci�n'
    dibujaPoblacion(poblacion)
    sleep(0.5)
    poblacion[100].sano=False
    
    



# Secci�n de la l�gica del programa.
poblacion =  creaPoblacion()

# Secci�n de la interfaz gr�fica.
ventana = Tk()
lienzo = Canvas(ventana, width = 404, height = 404)
lienzo.pack()
botonSalir = Button(ventana, text = "Salir", fg = "black", command = ventana.quit)
botonSalir.pack(side = LEFT)
boton1 = Button(ventana, text = "Corre simulaci�n", command = correSim)
boton1.pack(side = LEFT)
mainloop()
ventana.destroy()
