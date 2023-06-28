import os
os.system("cls")

name = input("Nombre: ")
tel = input("Telefono: ")
surName = input("Apellido: ")
age = input("Edad: ")
empresa = int(input("Año de ingreso: "))
if(empresa>2023):
    print("Año de ingreso invalido")
os.system("pause")
os.system("cls")
print(f"Nombre: {name}")
print(f"Apellido: {surName}")
print(f"Antiguedad en la empresa: {2023 - empresa}")
