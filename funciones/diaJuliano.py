print("\n\n")
fecha = input("Digite la fecha (dd/mm/aaaa): ")

dia = int(fecha[0:1])
mes = int(fecha[3:5])
anno = int(fecha[6:10])

feb = 0
dias =  0

if anno > 2999 or mes > 12 or dia > 31:
    print("fecha inválida")

elif mes == 2 or mes == '02' and dia > 29:
    print("fecha inválida")

else :
    if anno % 4 == 0 and (anno % 400 == 0 or anno % 100 != 0 ) :
            feb = 29
    else: 
        feb = 28

        diames = [31, feb, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        for i in range(mes-1):
            dias += diames[i]
        dias += dia    

        print(fecha, "es el dia ", dias, "del año ", anno)


print("\n\n")
