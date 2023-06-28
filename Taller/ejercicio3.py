import os
os.sytem("clear")

#Ejercicio 3
num = int(input("Ingresa un numero: "))
if(num > 0):
    print(f"El numero es positivo : {num}")
elif(num < 0):
    print(f"El numero es negativo : {num}")
else:
    print(f"El numero es cero : {num}")