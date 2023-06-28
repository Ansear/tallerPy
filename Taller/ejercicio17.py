import os 
os.system("cls")

num = input("Ingresa un numero: ")
tamaño = len(num)
acumulador = 0
while(tamaño>0):
    acumulador += int(num[tamaño-1])
    tamaño -= 1
print(f"Total : {acumulador}")
