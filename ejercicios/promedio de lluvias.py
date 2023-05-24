print("\n\n")

import random

abril = []
mayo = []
junio = []

for i in range(30):
    abril.append(random.uniform(0,11))
    mayo.append(random.uniform(0,11))
    junio.append(random.uniform(0,11))

pormAbril = sum(abril) * 1000 // len(abril) / 100
pormMayo = sum(mayo) * 1000 // len(mayo) / 100
pormJunio = sum(junio) * 1000 // len(junio) / 100

print("El promedio de lluvias en abril fue de " ,(pormAbril), " cm")
print("\nEl promedio de lluvias en mayo fue de " ,(pormMayo), " cm")
print("\nEl promedio de lluvias en junio fue de " ,(pormJunio), " cm")

if pormAbril > pormMayo and pormAbril > pormJunio :
    print("\n\nEl mes en que màs lloviò fue Abril")
elif pormMayo > pormAbril and pormMayo > pormJunio :
    print("\n\nEl mes en que màs lloviò fue Abril")
else :
    print("\n\nEl mes en que màs lloviò fue Junio")        


print("\n\n")
