import os
os.system("cls")
mes = input("Ingrese el nombre de un mes: ")

if(mes.upper() == "ENERO"):
    print(f"El mes {mes} tiene 31 dias")
elif(mes.upper() == "FEBRERO"):
    print(f"El mes {mes} tiene 28 dias")
elif(mes.upper() == "MARZO"):
    print(f"El mes {mes} tiene 31 dias")
elif(mes.upper() == "ABRIL"):
    print(f"El mes {mes} tiene 30 dias")
elif(mes.upper() == "MAYO"):
    print(f"El mes {mes} tiene 31 dias")
elif(mes.upper() == "JUNIO"):
    print(f"El mes {mes} tiene 30 dias")
elif(mes.upper() == "JULIO"):
    print(f"El mes {mes} tiene 31 dias")
elif(mes.upper() == "AGOSTO"):
    print(f"El mes {mes} tiene 31 dias")
elif(mes.upper() == "SEPTIEMBRE"):
    print(f"El mes {mes} tiene 30 dias")
elif(mes.upper() == "OCTUBRE"):
    print(f"El mes {mes} tiene 31 dias")
elif(mes.upper() == "NOVIEMBRE"):
    print(f"El mes {mes} tiene 30 dias")
elif(mes.upper() == "DICIEMBRE"):
    print(f"El mes {mes} tiene 31 dias")
else:
    print(f"El mes {mes} no existe")