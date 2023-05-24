print("\n\n")
print("*******BIENVENIDO A LA CALCULADORA*******\n\n")
uso = input("DESEA USAR LA CALCULADORA: ")
cantidadS = cantidadR = cantidadM = cantidadD = 0
while uso == "S" or uso == "s":
    print("SELECCIONA UNA OPERACION\n")
    print(" SUMA: S\n RESTA: R\n MULTIPLICACION: M\n DIVISION: D\n")
    pregunta = input("QUE OPERACION DESEAS REALIZAR: \n")
    num1 = int(input("Ingrese el primer digito: \n"))
    num2 = int(input("ingrese el segundo digito: \n"))
    if pregunta == "S" or pregunta == "s":
        print("la suma de ", num1, "con el ", num2, "es igual a ", num1+num2)
        cantidadS += 1
    elif pregunta == "R" or pregunta == "r":
        print("la resta de ", num1, "con el ", num2, "es igual a ", num1+num2)
        cantidadR += 1
    elif pregunta == "M" or pregunta == "n":
        print("la multiplicacion de ", num1, "con el ", num2, "es igual a ", num1+num2)
        cantidadM += 1
    elif pregunta == "D" or pregunta == "d":
        print("la division de ", num1, "con el ", num2, "es igual a ", num1+num2)
        cantidadD += 1
    uso = input("QUIERES HACER OTRA OPERACION: S/N  \n")
print("OPERACION \t\t", "CANTIDAD \n")
print("El total de sumas es de ",cantidadS,"\n")
print("El total de restas es de ",cantidadR,"\n")
print("El total de multiplicaciones es de ",cantidadM,"\n")
print("El total de divisions es de ",cantidadD,"\n")
print("GRACIAS POR USAR NUESTRA CALCULADORA!! \n")
            

                        




