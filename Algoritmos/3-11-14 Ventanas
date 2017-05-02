from Tkinter import *#importa la clase
root = Tk()#crea el objeto de la clase grafica
w=Label(root,text="Ola ke ase?")#crea la etiqueta en la ventana root y que el texto sea "ola ke ase?"
w.pack()
root.mainloop()#

class App:
    def __init__(self,master):
        frame = Frame(master)
        frame.pack()#cuando ya lo crearon deberia de meterlo en pack
        self.button = Button(
            frame, text="QUIT", fg="red", command=frame.quit
            )
        self.button.pack(side=LEFT)
        self.miboton=Button(
            frame,text="mi boton", fg="red", command=self.segundoBoton
            )
        self.miboton.pack(side=LEFT)

        self.hi_there=Button(frame,text="Hello", command=self.say_hi)
        self.hi_there.pack(side=LEFT)

    

    def say_hi(self):
        print "hi there, everyone!"

    def segundoBoton(self):
        print "Segundo Boton Presionado"
root = Tk()

app= App(root)
root.mainloop()
root.destroy()
