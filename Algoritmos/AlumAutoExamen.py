#                  
import random

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

def atenuaAgua(brillo, profundidad):    
    resultado=brillo
    for i in range(profundidad):
        resultado=resultado/1.0233
    return resultado

def limiteFotosintesis(valor):
    periodoPos=0
    while valor<=100:
        valor=valor*1.0233
        periodoPos+=1
    return periodoPos

def palindromo (cadena):
    return False

def dataCarbono14(valor):
    edad = 9 
    return edad

def name_to_number(name):
    if name == 'piedra':
        name = 0
    elif name == 'Spock':
        name = 1
    elif name == 'papel':
        name = 2
    elif name == 'lagarto':
        name = 3
    elif name == 'tijeras':
        name = 4
        

    # convierta name en number usando if/elif/else
    # recuerde devolver el resultado
    return name
    

def number_to_name(number):
    # borre la siguiente linea "pass" es para evitar el  error funcion vacia
    nombre = ''
    if number == 0:
        nombre = 'piedra'
    if number == 1:
        nombre = 'Spock'
    if number == 2:
        nombre = 'papel'
    if number == 3:
        nombre = 'lagarto'
    if number == 4:
        nombre = 'tijeras'
    # convierta number en name usando if/elif/else
    # recuerde devolver el resultado
    return nombre
    

def getComputer_choice():
    azar=random.randint(0,4)
    #genere un numero al azar entre 0 y 4 usando random.randint()
    
    # no olvide devolver el numero
    return azar
    
  

def rpsls(player_choice, comp_number):  
    ganador = 9
    # imprima una linea en blanco para separar los juegos
    
    # imprima el mensaje donde muestra la eleccion del jugador
    
    # convierta opcion "player_number" usando la funcion name_to_number()
    
    # convierta comp_number a comp_choice usando la funcion number_to_name()
    
    # imprima la eleccion de la computadora
    
    # calcule la diferencia de comp_number y player_number y saque el modulo 5
    
    # use if/elif/else para determinar al ganador
    return ganador
    # devuelva 0 si gana la computadora y 1 si gana jugador y 2 si es empate
    
    
## aqui puede colocar codigo para probar sus funciones, al terminar de probar, borrelo



# --- Codigo para calificacion automatica, no modificar (solo descomente su version de examen)

#Descomente la version que corresponda a su examen

ver = "a"
##ver = "b"   


def evalua_a():
    print "\n            Evaluando la version A del examen"
    aciertos = 0.0
    if mayor3(97, 14, 35) == 97:
        aciertos += 1
    if mayor3(44, 73, 33) == 73:
        aciertos += 1
    if mayor3(46, 83, 70) == 83:
        aciertos += 1
    if mayor3(33, 90, 11) == 90:
        aciertos += 1
    if mayor3(2, 72, 93) == 93:
        aciertos += 1
    if mayor3 (20, 20, 20) ==20:
        aciertos = aciertos + 1
    calif = aciertos  * 10 * 0.33333 / 6
    if limiteFotosintesis(1) == 200:
        calif = calif + 3.3334
    if limiteFotosintesis(1) == 201:
        calif = calif + 2.2222

    aciertos = 0.0
    if number_to_name(0) == "piedra":
        aciertos += 1
    if number_to_name(2) == "papel":
        aciertos += 1
    if name_to_number("Spock") == 1:
        aciertos += 1
    if name_to_number("lagarto") == 3:
        aciertos += 1
    if rpsls("piedra", 2) == 0:
        aciertos += 2
    if rpsls("papel", 1) == 1:
        aciertos += 2
    if rpsls("lagarto", 3) == 2:
        aciertos += 2
    calif = calif + aciertos/10 * 3.33334
    return calif

    

def evalua_b():
    print "\n             Evaluando la version B del examen"
    aciertos = 0.0
    if palindromo("ana")== True:
        aciertos = aciertos + 1
    if palindromo("radar")==True:
        aciertos = aciertos + 1
    if palindromo("marcelo")==False:
        aciertos = aciertos + 1
    if palindromo("casa")==False:
        aciertos = aciertos + 1
    
    calif = aciertos * 10 * 0.33333 / 4
    aciertos = 0.0
    if number_to_name(0) == "piedra":
        aciertos += 1
    if number_to_name(2) == "papel":
        aciertos += 1
    if name_to_number("Spock") == 1:
        aciertos += 1
    if name_to_number("lagarto") == 3:
        aciertos += 1
    if rpsls("piedra", 2) == 0:
        aciertos += 2
    if rpsls("papel", 1) == 1:
        aciertos += 2
    if rpsls("lagarto", 3) == 2:
        aciertos += 2
        
    calif = calif + aciertos/10 * 3.3334
    if dataCarbono14(25) == 11460:
        calif += 3.33334
    elif dataCarbono14(25) == (11460+5730):
        calif += 1.666666
        
    return calif



if ver=='a':
    calif = evalua_a()
else:
    calif = evalua_b()

print "\n  Su calificacion para la parte practica es: " + str(calif) 
print "  Por lo que suma "+ str(calif/2)+ " puntos para su examen \n"

