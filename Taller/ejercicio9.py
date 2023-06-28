import os
os.system("clear")

meses={
    "ENERO":31,
    "FEBRERO":28,
    "MARZO":31,
    "ABRIL":30,
    "MAYO":31,
    "JUNIO":30,
    "JULIO":31,
    "SEPTIEMBRE":30,
    "OCTUBRE":31,
    "NOVIEMBRE":30,
    "DICIEMBRE":31
}
dia = int(input("Ingresa el dia: "))
mes = input("Ingresa el mes, nombre: ")
año = int(input("Ingresa el año: "))

for i in range(len(meses)):
    if(año % 400 == 0) or (año % 4 == 0 and año % 100 != 0):
        meses["FEBRERO"] = 29
if(meses[mes.upper()] < dia):
    print(f"El dia {dia} no existe en el mes {mes}")
    print(f"La fecha es invalidad")    
else:
    print(f"La fecha es valida")