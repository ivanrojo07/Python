# -*- coding: cp1252 -*-
import re

def doble(valor):
    return valor * 2

a = "Esta es una cadena de prueba".split()
"Esta frase, contiene varias frases, separadas por comas".split()
"Esta frase, contiene varias frases, separadas por comas".split(',')

cad = "xaz123abc567zzabc12"
resultado = re.search('3', cad)
# Qu� buscar, d�nde buscar

print resultado.group()

m = re.search(r"\d\d\d", "hola402adios").group()
n = re.search(r"\d\d\d", "986hola").group()
o = re.search(r"\d\d\d", "adios1234").group()

# \d = [0123456789] En otras palabras, un d�gito del 0 al 9.
# \n Salto de l�nea.
# \t Tabulador.
# \w Cualquier n�mero o letra min�scula.
# \W Cualquier n�mero o letra may�scula.
# . Cualquier s�mbolo.
# \s Espacio en blanco, salto de l�nea, tabulador.
# ^ (Circunflejo). Significa 'inicio de la cadena' y busca aquello que inicie con ese par�metro.
# $ Fin de cadena.
