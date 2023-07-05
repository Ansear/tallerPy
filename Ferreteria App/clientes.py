import core 
import os
def createData(*args):
    return core.loadInfo("clientes.json")

def mainMenu():
    os.system("clear")
    isCliRun = True
    print('+','-'*66,'+')
    print("|{:^15}{}{:^20}|".format(' ','ADMINISTRACION DE CLIENTES',' '))
    print('+','-'*66,'+')
    while (isCliRun):
        print("1. Crear Cliente")
        print("2. Editar Cliente")
        print("3. Buscar Cliente")
        print("4. Regresar al menu principal")
        opcion = int(input(":)"))
        if(opcion == 1):
            mainMenu()
            pass
        elif(opcion == 2):
            pass
        elif(opcion == 3):
            pass
        elif(opcion == 4):
            isCliRun = False