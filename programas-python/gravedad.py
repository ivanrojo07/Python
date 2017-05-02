#--------------------------------------------------------------------
# Módulo: gravedad
#
# Propósito: proporciona algunas constantes y funciones sobre física gravitatoria.
#
# Autor/es: Isaac Pérez González y Alberto Pérez López
#--------------------------------------------------------------------
# Constantes exportadas:
# \qquad$G$: Constante de gravitación universal.
# \qquad\emph{M\texttt{_}Tierra}: Masa de la Tierra (en kilos).
# \qquad\emph{R\texttt{_}Tierra}: Radio de la Tierra (en metros).
# \qquad\emph{M\texttt{_}Luna}: Masa de la Luna (en kilos).
# \qquad\emph{R\texttt{_}Luna}: Radio de la Luna (en metros).
#
# Funciones exportadas:
# \qquad\emph{fuerza\texttt{_}grav} : calcula la fuerza gravitatoria existente entre dos cuerpos.
# \qquad\quad entradas:
# \qquad\qquad$M$: masa de un cuerpo (en kg).
# \qquad\qquad$m$: masa del otro cuerpo (en kg).
# \qquad\qquad$r$: distancia entre ellos (en metros).
# \qquad\quad salida:
# \qquad\qquad fuerza (en Newtons).
#          
# \qquad\emph{distancia} : calcula la distancia que separa dos cuerpos atraídos por una fuerza 
# \qquad\qquad\qquad\qquad gravitatoria determinada.
# \qquad\quad entradas:
# \qquad\qquad $M$: masa de un cuerpo (en kg).
# \qquad\qquad $m$: masa del otro cuerpo (en kg).
# \qquad\qquad $F$: fuerza gravitatoria experimentada (en m).
# \qquad\quad salida:
# \qquad\qquad distancia (en metros).
#
# \qquad\emph{velocidad\texttt{_}escape}: calcula la velocidad necesaria para escapar de la atracción 
# \qquad\qquad\qquad\qquad gravitatoria de un cuerpo esférico.
# \qquad\quad entradas:
# \qquad\qquad $M$: masa del cuerpo (en kg).
# \qquad\qquad $R$: radio del cuerpo (en metros).
# \qquad\quad salida:
# \qquad\qquad velocidad (en metros por segundo).
#------------------------------------------------------------------
# Historia:
# \qquad * Creado el 13/11/2001 por Isaac 
# \qquad * Modificado el 15/11/2001 por Alberto:
# \qquad\qquad - se incluyen las constantes \emph{M\texttt{_}Luna} y \emph{R\texttt{_}Luna}
# \qquad\qquad - se añade la función \emph{velocidad\texttt{_}escape}
#------------------------------------------------------------------
from math import sqrt

G = 6.67e-11
M_Tierra = 5.97e24
R_Tierra = 6.37e6
M_Luna = 7.35e22
R_Luna = 1.74e6

def fuerza_grav(M, m, r):
  return G * M * m / r**2

def distancia(M, m, F):
  return sqrt( G * M * m / F )

def velocidad_escape(M, R):
  return sqrt( 2 * G * M / R )

ve_Tierra = velocidad_escape(M_Tierra, R_Tierra)
ve_Luna = velocidad_escape(M_Luna, R_Luna)
