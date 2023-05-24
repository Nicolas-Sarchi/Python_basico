print("\n\n")

estudiantes = int(input("Digite el nùmero de estudiantes: "))
est = []

for i in range(estudiantes):
    nombre = input(" Digite su nombre: ")
    n1 = float(input("\ndigite la primera nota: "))
    n2 = float(input("\ndigite la segunda nota: "))
    n3 = float(input("\ndigite la tercera nota: "))
    prom = round((n1 + n2 + n3) / 3, 2)
    est.append([nombre, n1, n2, n3, prom])

print("\nNombre \t\tN1 \t\tN2 \t\tN3 \t\tPromedio")
for i in est:
    print(i[0], "\t\t", i[1], "\t\t", i[2], "\t\t", i[3], "\t\t", i[4])

print("\n\n")
# alumnos = ['nombre', 'n1', 'n2', 'n3', 'prom']