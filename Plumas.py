c = int(raw_input("Escribe el valor de plumas que compraras: "))
NoPaqEnt = [1,2,3,4,6,7,9,11,12,14,17,19,22,27]
def esPar (num):
    if(num in NoPaqEnt):
        return False
    else:
        return True
print (c, esPar(c))
