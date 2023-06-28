import os

import os
os.system("cler")

#ejercicio 10
lon1 = int(input("Ingresa longitud 1: "))
lon2 = int(input("Ingresa longitud 2: "))
lon3 = int(input("Ingresa longitud 3: "))

a = lon1+lon2
b = lon1+lon3
c = lon2+lon3
if(a>lon3 and b>lon2 and c>lon1):
    print("Si se puede formar un triandulo")
else:
    print("No se puede formar un triandulo")