import os
os.system("clear")
#Ejercicio 2
num = int(input("Ingresa un numero entero positivo: "))
if(num >0):
    while(num >= 1):
        print(f"Numero entero: {num}")
        num -= 1
else:
    print(f"El numero debe ser entero positivo: {num}")