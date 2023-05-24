# Dada la siguiente información sobre las calificaciones de estudiantes de una institución educativa:
# • Código
# • Nombre
# • Nota 1 (Peso de 30%)
# • Nota 2 (Peso de 30%)
# • Nota 3 (Peso de 40%)
# El proceso se termina cuando el código que se ingrese sea 999.(Bandera)
# Se pide calcular:

# La nota definitiva de cada estudiante e indicar con un mensaje si aprobó o reprobó, utilizando funciones
# Para aprobar, la nota deber ser mayor o igual a 3.0 y la información en su totalidad se debe almacenar
# en listas

print("\n\n")

def calcular_nota(nota1, nota2, nota3):
    notaDef = round(nota1 * 0.3 + nota3 * 0.3 + nota3 * 0.4,2)
    return notaDef

def aprobacion(nota):
    if nota >= 3 :
        est ="APROBADO"
    else :
        est = "REPROBADO" 
    return est

codigos = []
nombres = []
notas = []

while True:
    codigo = int(input("\nIngrese el còdigo del estudiante (999 para salir): "))
    if codigo == 999 :
        break

    nombre = input("\nNombre: ")
    nota1 = float(input("Nota 1 (30%): "))
    nota2 = float(input("Nota 2 (30%): "))
    nota3 = float(input("Nota 3 (40%): "))

    nota_definitiva = calcular_nota(nota1, nota2, nota3)
    aprobado = aprobacion(nota_definitiva)

    codigos.append(codigo)
    nombres.append(nombre)
    notas.append(nota_definitiva)

print("\n\t\t------INFO ESTUDIANTES------")    
for i in range(len(codigos)):
    print("Còdigo: ", codigos[i], "\t\tNombre: ", nombres[i], "\t\tNota definitiva: ", notas[i], "\t\tEstado: " , aprobacion(notas[i]))


print("\n\n")
