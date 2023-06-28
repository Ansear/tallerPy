import os
os.system("clear")
#ejercicio 8

pais = input("Ingresa el nombre del pais: ")
america= ["ESTADOS UNIDOS", "CANADA", "MEXICO","BRASIL", "ARGENTINA", "COLOMBIA", "PERU"]
europa = ["ALEMANIA", "FRANCIA", "REINO UNIDO", "ITALIA"]
asia = ["CHINA", "INDIA", "JAPON", "RUSIA"]
oceania = ["AUSTRALIA","NUEVA ZELANDA","PAPUA NUEVA GUINEA"]
africa = ["SUDAFRICA","NIGERIA","EGIPTO","KENIA"]
oki=False
while(oki==False):
    for i in range(len(america)):
        if(pais.upper() == america[i]):
            print(f"{pais} esta en Ameria")
            oki=True
            break
    for i in range(len(europa)):
        if(pais.upper() == europa[i]):
            print(f"{pais} esta en Europa")
            oki=True
            break
    for i in range(len(asia)):
        if(pais.upper() == asia[i]):
            print(f"{pais} esta en Asia")
            oki=True
            break
    for i in range(len(oceania)):
        if(pais.upper() == oceania[i]):
            print(f"{pais} esta en Oceania")
            oki=True
            break
    for i in range(len(africa)):
        if(pais.upper() == africa[i]):
            print(f"{pais} esta en Africa")
            oki=True
            break
    if(oki==False):
        print(f"{pais} no se encuentra")
        oki=True
        break
