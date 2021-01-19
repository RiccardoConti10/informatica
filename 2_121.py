import math 

def calcolo_delta (a, b, c) :
    variabile = math.pow(b, 2) - 4 * a * c 
    return variabile 

def calcolo_vertice (a, b, c) : 
    delta = calcolo_delta (a, b, c)
    X_vertice = - (b/(2*a))
    Y_vertice = - (delta/(4*a))
    return X_vertice, Y_vertice

def calcolo_fuoco(a, b, c):
    delta = calcolo_delta(a, b, c)
    X_fuoco = -(b/(2*a))
    Y_fuoco = (1 - delta)/(4*a)
    return X_fuoco, Y_fuoco

def main () :
    a = int (input ("scrivi il valore di a"))
    b = int (input ("scrivi il valore di b"))
    c = int (input ("scrivi il valore di c"))

    scelta = int (input ("scegli cosa calcolare, premi 1 per calcolare il vertice, 2 per calcolare il fuoco, se vuoi andartene premi 0 e premi 3 per calcolare sia vertice sia fuoco"))
    if scelta == 1:
        print (calcolo_vertice(a, b, c))
    elif scelta == 2:
        print (calcolo_fuoco(a, b, c))
    elif scelta == 0:
        print ("ciao alla prossima")
    elif scelta == 3:
        print (calcolo_vertice(a, b, c))
        print (calcolo_fuoco(a, b, c))
    else:
        print ("hai sbagliato tasto da premere")   

main()
