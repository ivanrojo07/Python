import pickle

# Leemos la lista carg�ndola del fichero \texttt{mifichero.mio}...
lista = pickle.load(open('mifichero.mio'))
# y la mostramos por pantalla.
print lista
