# Programa:  }  \COM{\texttt{rectangulo.py}
# Prop�sito: }  \COM{Calcula el per�metro y el �rea de un rect�ngulo a partir 
#            }  \COM{de su altura y anchura.
# Autor:     }  \COM{John Cleese
# Fecha:     }  \COM{1/1/2001

# Petici�n de los datos (en metros)
altura = float(raw_input('Dame la altura (en metros): '))  
anchura = float(raw_input('Dame la anchura (en metros): '))

# C�lculo del �rea y del per�metro
area = altura * anchura                                    
perimetro = 2 * altura + 2 * anchura                        

# Impresi�n de resultados por pantalla
print 'El per�metro es de %6.2f metros' % perimetro  # s�lo dos decimales.
print 'El �rea es de %6.2f metros cuadrados' % area
