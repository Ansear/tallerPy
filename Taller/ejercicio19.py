import os
os.system("clear")

kwMes = int(input("Ingrese el total de kw consumidos: "))
estrato = int(input("Ingresa tu estrado: "))
valorKw = 500
if(estrato == 1):
    print(f"Total de kw consumidos: {kwMes}")
    print(f"Mes de consumo: {kwMes * valorKw}")
elif(estrato == 2):
    print(f"Total de kw consumidos: {kwMes}")
    total=(kwMes * valorKw)*1.10
    print(f"Mes de consumo: {total}")
elif(estrato == 3):
    print(f"Total de kw consumidos: {kwMes}")
    total=(kwMes * valorKw)*1.20
    print(f"Mes de consumo: {total}")
elif(estrato == 4):
    print(f"Total de kw consumidos: {kwMes}")
    total=(kwMes * valorKw)*1.30
    print(f"Mes de consumo: {total}")
elif(estrato == 5):
    print(f"Total de kw consumidos: {kwMes}")
    total=(kwMes * valorKw)*1.40
    print(f"Mes de consumo: {total}")
