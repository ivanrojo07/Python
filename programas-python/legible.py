print 'Programa para el c�lculo del per�metro y el �rea de un rect�ngulo.'

altura = float(raw_input('Dame la altura (en metros): '))   
anchura = float(raw_input('Dame la anchura (en metros): ')) 

area = altura * anchura                                     
perimetro = 2 * altura + 2 * anchura                        

print 'El per�metro es de %6.2f metros.' % perimetro         
print 'El �rea es de %6.2f metros cuadrados.' % area         
