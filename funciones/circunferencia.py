# Diseñar una función que calcule el área y el perímetro de una circunferencia. Utiliza dicha función en un programa principal que lea el radio de una circunferencia y muestre su área y perímetro.
import math
import cmath
pi = math.pi
print("\n\n")

def circunferencia(radio):
    area = round(pi ** radio,2)
    perimetro =round( 2 * pi * radio,2)
    
    return area, perimetro

radio = float(input("Ingrese el valor del radio de su circunferencia: "))

print("Los valores del área y el perimetro de su círculo son: " , circunferencia(radio))
print("\n\n")
