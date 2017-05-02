# -*- coding: cp1252 -*-
import re

def doble(valor):
    return valor * 2

a = "Esta es una cadena de prueba".split()
"Esta frase, contiene varias frases, separadas por comas".split()
"Esta frase, contiene varias frases, separadas por comas".split(',')

cad = "xaz123abc567zzabc12"
resultado = re.search('3', cad)
# Qué buscar, dónde buscar

print resultado.group()

m = re.search(r"\d\d\d", "hola402adios").group()
n = re.search(r"\d\d\d", "986hola").group()
o = re.search(r"\d\d\d", "adios1234").group()

# \d = [0123456789] En otras palabras, un dígito del 0 al 9.
# \n Salto de línea.
# \t Tabulador.
# \w Cualquier número o letra minúscula.
# \W Cualquier número o letra mayúscula.
# . Cualquier símbolo.
# \s Espacio en blanco, salto de línea, tabulador.
# ^ (Circunflejo). Significa 'inicio de la cadena' y busca aquello que inicie con ese parámetro.
# $ Fin de cadena.
