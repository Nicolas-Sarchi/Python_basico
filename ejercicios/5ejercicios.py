import math
import cmath
pi = math.pi

def aCirculo():
    rad = float(input("\nIngrese el radio del circulo: "))
    area = pi * (rad ** 2)
    return f"area: {area}"

def atriangulo():
    b = float(input("\nIngrese valor de la Base: "))
    h = float(input("\nIngrese valor Altura"))
    return f"Area: {(b * h) / 2}"

def aCuadrado():
    m = 1
    for i in range(2):
        l = float(input(f"Ingrese el valor del lado {i+1}: "))
        m *= l
    return f"Area: {m}"
def punto1(opcion):
    if opcion == 1:
        resultado = aCirculo()
        print(resultado)
    elif opcion == 2:
        resultado = atriangulo()
        print(resultado)
    else:
        resultado = aCuadrado()
        print(resultado)
def numeroPrimo(num):
    if num < 2:
        return False
    for i in range(2,int(num ** 0.5)+1):
        if num % i == 0:
            return False
    return True
def factorial():
    valor = int(input("ingrese el numero que desea calcular: "))
    fac = 1
    for i in range(valor):
        fac *= (i+1)
    return f"El factorial de {valor}: {fac}"

def punto4(monto,opcion):
    if opcion == 1 : 
        cambio = 0.00021
        sim = "dòlares"
    elif opcion == 2 :
        cambio = 0.028
        sim = "yenes"
    elif opcion == 3:
        cambio = 0.00017
        sim = "libras"
    else:
        print("Opcion invàlida")  
    conversion = monto * cambio
    return f"{monto} COP es equivalente a {conversion} {sim} "   
            # db**2)-(4*a*c)
def cuadratica (a, b, c,):
    disc = (b**2)-(4*a*c)
    sol1 = (-b-cmath.sqrt(disc)) / (2*a)
    sol2 = (-b+cmath.sqrt(disc)) / (2*a)
    if disc < 0:
            print("La ecuación tiene soluciones imaginarias.")
    else:
            print("Las soluciones de la ecuación son:")
            print("x1 = ", sol1)
            print("x2 = ", sol2)



veces = int(input("\nDigite la cantidad de veces que desea usar la aplicaciòn "))

for i in range(veces):
    print("""\n\nMENU GENERAL
    1. APLICACION 1
    2. APLICACION 2
    3. APLICACION 3
    4. APLICACION 4
    5. APLICACION 5""")
    op = int(input("opcion: "))
    if op == 1:
       
            print("""MENU
            1. CALCULO AREA CIRCULO
            2. CALCULO AREA TRIANGULO
            3. CALCULO AREA CUADRADO""")
            op1 = int(input("opcion: "))
            punto1(op1)
                   
    elif op == 2:
        numero = int(input("ingrese el numero que desea calcular: "))
        d = numeroPrimo(numero)
        print(d)
             
    elif op == 3:
        print(factorial())
        
    elif op == 4:
        print("""MENU
        1. DE COP A USD
        2. DE COP A JPY
        3. DE COP A GBP""")
        op2 =int(input("Opcion: "))
        
        monto = float(input("Ingrese la cantidad que desea convertir: "))
        print(punto4(monto, op2))
            
    elif op == 5 :
        a = float(input("Ingrese el valor de a: "))
        b = float(input("ingrese el valor de b: "))
        c = float(input("ingrese el valor de c: "))
        
        print (cuadratica(a,b,c))
    else: 
        print("Opciòn invàlida")    