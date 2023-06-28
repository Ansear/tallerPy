import os
os.system("cls")

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
dia = input("Ingresa el dia: ")
mes = input("Ingresa el mes, nombre: ")
año = input("Ingresa el año: ")

for i in range(len(meses)):
    if(año % 400 == 0) or (año % 4 == 0 and año % 100 != 0):
        meses["FEBRERO"] = 29