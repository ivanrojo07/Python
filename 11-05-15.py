instruccion="LDV 1; STA a;"
instruccion= instruccion.split(';')
inst=instruccion[0:3]
param=instruccion[4:len(instruccion)-1]
pc=[]
acu=[]
print inst
print param
if (inst == "LDV"):
    pc= param
else:
    pc= pc+1
