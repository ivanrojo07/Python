# Programa:  }  \COM{\texttt{rectangulo.py}
# Propósito: }  \COM{Calcula el perímetro y el área de un rectángulo a partir 
#            }  \COM{de su altura y anchura.
# Autor:     }  \COM{John Cleese
# Fecha:     }  \COM{1/1/2001

# Petición de los datos (en metros)
altura = float(raw_input('Dame la altura (en metros): '))  
anchura = float(raw_input('Dame la anchura (en metros): '))

# Cálculo del área y del perímetro
area = altura * anchura                                    
perimetro = 2 * altura + 2 * anchura                        

# Impresión de resultados por pantalla
print 'El perímetro es de %6.2f metros' % perimetro  # sólo dos decimales.
print 'El área es de %6.2f metros cuadrados' % area
