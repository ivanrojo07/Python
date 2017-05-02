def numCasos(base,numPeriodos):
    resultado = base
    for c in range (numPeriodos):
        resultado= resultado *1.3742
    return int (resultado)

print numCasos(72,13)
print 'diciembre 2014',numCasos(72,18)
print 'octubre 15', numCasos(72,37)
print 'octubre 16', numCasos(72,61)

