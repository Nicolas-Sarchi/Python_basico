print('\n\n\n')
matriz = [[2,8,9,8],[5,8,7,5],[2,8,9,6]]
inp=""
for filas in range(3): 
    for valor in range(4):
        inp+= str(matriz[filas][valor])+ "\t"
    print(inp)
    inp=""

print('\n\n\n')
