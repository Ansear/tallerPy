import os
os.system("clear")
#Ejercicio 5 
ban = False
pas = input("Ingresa la contraseña: ")
length = len(pas)
for i in range(length):
    if(pas[i].isdigit()):
        ban = True
if(ban and length>=8):
    print("Contraseña Valida")
else: 
    print("Contraseña Invalida")