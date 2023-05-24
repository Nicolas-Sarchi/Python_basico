print("\n\n")

def factorial(valor):
    fac = 1
    for i in range(valor):
        fac *= (i+1)
    return fac    
        
        
valor = int(input("ingrese el numero a calcular: "))   

print("El factorial de", valor, "es: ", factorial(valor))     

print("\n\n")
       