# -*- coding: cp1252 -*-
#Rojo Orea Guillermo Iván
def leeArchivo():
    lectura = open('uno.txt','r')
    renglon = lectura.read()
    renglon = renglon.lower()
    return renglon

def esTipoDato(palabra):
    return palabra in ['string', 'integer', 'real', 'bool']

listaTokens = ['var', 'nombre', ':', 'string', ';', 'var', 'edad', ':', 'integer', ';', 'var', 'horas', ':', 'integer', ';', 'var', 'sueldo', ':', 'real', ';']
tablaDatos = []
listaTokens = []
LF=[]

def ensa(CI):
    op='+-*/'
    ens=['LDV','STA','LDA','ADD','SUB','MUL','DIV','JZ','JMP','IN4']
    r=[]
    s=0
    d=''
    c=''
    jmp=0
    inc=''
    op1=''
    op2=''
    while CI != []:
        b=CI.pop(0)
        if 'for' in b[0]:
            for i in range(len(b)):
                for j in b[i]:
                    if s==4:
                        if j == 'print':
                            r.append(ens[len(ens)-1]+' '+b[i][2]+';')
                            s=0
                        else:
                            for k in j:
                                if esOperador(k):
                                    k = InfPos(k)                        
                                    while k != []:
                                        for i in k:
                                            if esOperador(i):
                                                s=k.index(i)
                                                d=k.pop(k.index(i))
                                                if k != []:
                                                    op2=k.pop(s-1)
                                                if k != []:
                                                    op1=k.pop(s-2)
                                                if op1 != '':
                                                    r.append(ens[2]+' '+op1+';')
                                                if op2 != '':
                                                    r.append(ens[op.find(d)+3]+' '+op2+';')
                                            op1=''
                                            op2=''
                                    s=0
                                    r.append(ens[1]+' '+j[0]+';')
                                else:
                                    s=1
                            if s==1:
                                r.append(ens[0]+' '+j[2]+';')
                                r.append(ens[1]+' '+j[0]+';')
                                c=j[0]
                                s=0
                    if j=='for':
                        s=4
                    else:
                        if s==1:
                            s=0
                            r.append(d+' '+str(j+1)+';')
                            r.append('JZ')
                        if j == 'SUB':
                            s=1
                            d=j
                            r.append(ens[2]+' '+c+';')
                            jmp=len(r)
                        if s==2:
                            s=0
                            inc=(d+' '+c+';')
                        if j == 'INC':
                            s=2
                            d=j
        else:
            for i in b:
                if str(i) in op:
                    k = InfPos(i)                        
                    while k != []:
                        for i in k:
                            if esOperador(i):
                                s=k.index(i)
                                d=k.pop(k.index(i))
                                if k != []:
                                    op2=k.pop(s-1)
                                if k != []:
                                    op1=k.pop(s-2)
                                if op1 != '':
                                    r.append(ens[2]+' '+op1+';')
                                if op2 != '':
                                    r.append(ens[op.find(d)+3]+' '+op2+';')
                            op1=''
                            op2=''
                    s=0
                else:
                    s=1
            if s==1:
                r.append(ens[0]+' '+str(b[2])+';')
                r.append(ens[1]+' '+str(b[0])+';')
    if inc != '':
        r.append(inc) 
        r.append('JMP'+' '+str(jmp)+';')                
        r[r.index('JZ')]= 'JZ '+str(len(r))+';'            
    return r

def var(listaTokens):
    nuevoDato = []
    f=0
    cu=0
    for i in range(len(listaTokens)):
        j = listaTokens[i]        
        if j == 'var':
            nuevoDato.append(listaTokens[i + 1])
        if esTipoDato(j):
            nuevoDato.append(j)
            if j == 'string':
                nuevoDato.append('Null')
            elif j == 'integer':
                nuevoDato.append(0)
            elif j == 'real':
                nuevoDato.append(0.0)
            elif j == 'bool':
                nuevoDato.append(False)
            tablaDatos.append(nuevoDato)
            nuevoDato = []

def listokens(renglon):
    cad =""
    res = []
    for i in renglon:
        if i in " ;:\n(),+-*/^<>=!{}":
            if cad != "":
                listaTokens.append(cad)
                cad=""
            if i in ";:(),+-*/^<>=!{}":
                listaTokens.append(i)
        else:
            cad = cad + i

def esOperador (a):
    for i in a:
        c = i in "+-*/^"
        if c == True:
            break
    return c

def mayorPre (a,b):
    op = ["+-","*/","^"]
    c=0
    d=0
    for i in range(len(op)):
        if (a in op[i]):
            c = i+1
        if (b in op[i]):
            d = i+1
    return (c>=d)

def InfPos(infija):
    p=0
    pila = []
    pilaTemp=[]
    salida=[]
    for e in infija:
        if (e == "("):
            p=1
        elif (e == ")"):
            while (len(pilaTemp) != 0):
                salida.append(pilaTemp.pop())
                p=0
        elif (esOperador(e) and p==0):
            while (len(pila) != 0 and (mayorPre(pila[len(pila)-1],e))):
                salida.append(pila.pop())
            pila.append(e)
        else:
            if (p==0):
                salida.append(e)
            else:
                if (esOperador(e)):
                    while (len(pilaTemp) != 0 and (mayorPre(pilaTemp[len(pilaTemp)-1],e))):
                        salida.append(pilaTemp.pop())
                    pilaTemp.append(e)
                else:
                    salida.append(e)       
    while (len(pila) != 0):
        salida.append(pila.pop())
    return salida

def ope(op1,op2,i):
    c=[]
    d=0
    for j in range(len(tablaDatos)):
        c.append(tablaDatos[j][0])
    if op1 in c:
        op1=tablaDatos[c.index(op1)][2]
    else:
        op1=int(op1)
    if op2 in c:
        op2=tablaDatos[c.index(op2)][2]
    else:
        op2=int(op2)
    if i == '+':
        d=op1+op2
    if i == '-':
        d=op1-op2
    if i == '*':
        d=op1*op2
    if i == '/':
        d=op1/op2
    if i == '^':
        d=op1^op2  
    return d

def resol(formula):
    a=''
    b=[]
    pil=[]
    op1=0
    op2=0
    for i in formula:
        if i in "+-*/^()":
            if a!='':
                b.append(a)
            b.append(i)
            a=''
        else:
            a=a+i
    if a != '':
        b.append(a)
    a= InfPos(b)
    for i in a:
        if esOperador(i):
            op1=pil.pop(0)
            op2=pil.pop(0)
            pil.append(ope(op1,op2,i))
        else:
            pil.append(i)
    return pil.pop()

def ciclof(cf):
    vr=[]
    vr1=[]
    d=''
    inc=0
    for i in range(len(cf)):
        if cf[i] == '(':
            i=i+1
            while cf[i] != ';':
                vr1.append(cf[i])
                i=i+1
            vr.append(vr1)
            LF.append(['for',vr1])
            vr1=[]
            i=i+1
            while cf[i] != ';':
                if cf[i] in '<>=':
                    d=d+cf[i]
                else:
                    if d != '':
                        vr1.append(d)
                        d=''
                    vr1.append(cf[i])
                i=i+1
            vr.append(vr1)
            vr1=[]
            i=i+1
            while cf[i] != ')':
                vr1.append(cf[i])
                i=i+1
            vr.append(vr1)
            vr1=[]
            LF.append(['SUB',int(vr[1][2])-int(vr[0][2])])
            if vr[2][2] == '+':
                LF.append(['INC',1])
            else:
                LF.append(['INC',vr[2][len(vr[2])-1]])
        if cf[i] == '{':
            while(cf[i] != '}'):
                if cf[i] == '=':
                    vr1.append(cf[i-1])
                    vr1.append(cf[i])
                    i=i+1
                    while(cf[i] != ';'):
                        d=d+cf[i]
                        i=i+1
                    vr1.append(d)
                    LF.append(['for',vr1])
                i=i+1
                vr1=[]
                d=''
                if cf[i] == 'print':
                    LF.append(['for','print',cf[i+2]])
            break
                        

def asigvar(listatokens):
    c=0
    d=''
    de=False
    e=1
    var=[]
    var1=[]
    asig = ['+','-','*','/','(',')','^','=']
    imp=[]
    fo=[]
    for i in listatokens:
        if de == True:
            fo.append(i)
        if i=='}':
            de = False
            ciclof(fo)
            var.append(LF)
        if i == 'for'and de == False:
            de=True
        if i == '=' and de == False:
            while(listatokens[c+e]!=';'):
                d=d+listatokens[c+e]
                e=e+1
            var1.append(listatokens[c-1])
            var1.append(i)
            var1.append(d)
            var.append(var1)
            d=''
            e=1
            var1=[] 
        if i == 'print' and de == False:
            imp.append(listatokens[c+2])
        c=c+1
    c=0
    for j in range(len(tablaDatos)):
        var1.append(tablaDatos[j][0])
    for i in var:
        if i[0] in var1:
            for j in i[2]:
                if j in asig:
                    de=True
            if de == True:
                var[c][2] = resol(var[c][2])
                de=False
            if tablaDatos[var1.index(i[0])][1] == 'integer':
                tablaDatos[var1.index(i[0])][2]=int(var[c][2])
            if tablaDatos[var1.index(i[0])][1] == 'string':
                tablaDatos[var1.index(i[0])][2]=var[c][2]
            if tablaDatos[var1.index(i[0])][1] == 'real':
                tablaDatos[var1.index(i[0])][2]=float(var[c][2])
            if tablaDatos[var1.index(i[0])][1] == 'bool':
                if var[var1.index(i[0])][2]== 'false':
                    tablaDatos[var1.index(i[0])][2]=False
                else:
                    tabl
                    aDatos[var1.index(i[0])][2]=True
        c=c+1
        if 'for' in i[0]:
            for k in range(i[1][1]):
                tablaDatos[var1.index(i[0][1][0])][2]=tablaDatos[var1.index(i[0][1][0])][2]+int(i[2][1])
                for h in i[3:len(i)-1]:
                    for l in h[1]:
                        if l in asig:
                            de=True
                    if de == True:
                        tablaDatos[var1.index(h[1][0])][2] = resol(h[1][2])
                        de=False
                for m in i:
                    if 'print' in m:
                        imp.append(tablaDatos[var1.index(m[2])][2])
    return imp, var
    
listokens(leeArchivo())
var(listaTokens)
var=asigvar(listaTokens)
LF=ensa(var[1])

for i in var[0]:
    for j in range(len(tablaDatos)):
        if(i==tablaDatos[j][0]):
            print tablaDatos[j][2]
for i in tablaDatos:
    print i
