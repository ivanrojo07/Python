def mayor2(a,b):
    
    if (a>b):
       mayordos= a
       if (b>a):
           mayordos= b

    elif a==b:
        mayordos= a
    else:
        mayordos = b
# escriba aqui
    return mayordos
        

def mayor3(a, b, c):
    mayortres= mayor2((mayor2(a,b)),(mayor2(b,c)))
    return mayortres
