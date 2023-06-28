import os 
os.system("cls")
val = False
acumulador = 0
cont = 0
while(val==False):
    num = int(input("Ingresa un numero positivo: "))

    if(num>0):
        acumulador += num
        cont += 1
        val = False
    else:
        val = True
print(f"promedio: {acumulador/cont}")
