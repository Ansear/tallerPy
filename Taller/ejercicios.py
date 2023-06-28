import os
#Ejercicio 1
# age = int(input("Ingresa tu edad: "))

# if age >= 18:
#     print("Eres mayor de edad")
# else:
#     print("Eres menor de edad")

#Ejercicio 2
# num = int(input("Ingresa un numero entero positivo: "))
# if(num >0):
#     while(num >= 1):
#         print(f"Numero entero: {num}")
#         num -= 1
# else:
#     print(f"El numero debe ser entero positivo: {num}")

#Ejercicio 3
# num = int(input("Ingresa un numero: "))
# if(num > 0):
#     print(f"El numero es positivo : {num}")
# elif(num < 0):
#     print(f"El numero es negativo : {num}")
# else:
#     print(f"El numero es cero : {num}")

#Ejercicio 4
# os.system("cls")
# num = int(input("Ingresa un numero: "))
# if(num%2 == 0):
#     print(f"El numero es par: {num}")

#Ejercicio 5 
# os.system("cls")
# ban = False
# pas = input("Ingresa la contraseña: ")
# length = len(pas)
# for i in range(length):
#     if(pas[i].isdigit()):
#         ban = True
# if(ban and length>=8):
#     print("Contraseña Valida")
# else: 
#     print("Contraseña Invalida")

#Ejercicio 6
# os.system("cls")
# exa = int(input("Ingresa su calificación: "))
# if(exa >=60) :
#     print(f"Has Aprobado, Calificacion: {exa}")
# else:
#     print(f"Has Reprobado, Calificacion: {exa}")

#Ejercicio 7
# os.system("cls")
# pas = input("Ingresa la contraseña: ")
# if(pas == "secreto123"):
#     print("Acceso Permitido")
# else:
#     print("Acceso Denegado")

#ejercicio 8
# os.system("cls")
# pais = input("Ingresa el nombre del pais: ")
# america= ["ESTADOS UNIDOS", "CANADA", "MEXICO","BRASIL", "ARGENTINA", "COLOMBIA", "PERU"]
# europa = ["ALEMANIA", "FRANCIA", "REINO UNIDO", "ITALIA"]
# asia = ["CHINA", "INDIA", "JAPON", "RUSIA"]
# oceania = ["AUSTRALIA","NUEVA ZELANDA","PAPUA NUEVA GUINEA"]
# africa = ["SUDAFRICA","NIGERIA","EGIPTO","KENIA"]
# oki=False
# while(oki==False):
#     for i in range(len(america)):
#         if(pais.upper() == america[i]):
#             print(f"{pais} esta en Ameria")
#             oki=True
#             break
#     for i in range(len(europa)):
#         if(pais.upper() == europa[i]):
#             print(f"{pais} esta en Europa")
#             oki=True
#             break
#     for i in range(len(asia)):
#         if(pais.upper() == asia[i]):
#             print(f"{pais} esta en Asia")
#             oki=True
#             break
#     for i in range(len(oceania)):
#         if(pais.upper() == oceania[i]):
#             print(f"{pais} esta en Oceania")
#             oki=True
#             break
#     for i in range(len(africa)):
#         if(pais.upper() == africa[i]):
#             print(f"{pais} esta en Africa")
#             oki=True
#             break
#     if(oki==False):
#         print(f"{pais} no se encuentra")
#         oki=True
#         break

#ejercicio 10
os.system("cls")
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