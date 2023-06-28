import os
os.system("clear")
flag = True
flagA = False
flagS = False
while(flag):
    os.system("clear")
    print("---------------MENU---------------")
    print("1.  CREAR GRUPO ARTEMIS:")
    print("1.1 LISTAR CAMPERS DE ARTEMIS")
    print("1.2 AGREGAR CAMPERS A ARTEMIS")
    print("1.3 ELIMINAR CAMPERS A ARTEMIS")
    print("1.4 ORDENAR ALFABETICAMENTE EN LISTA DE ARTEMIS")
    print("1.5 BUSCAR CAMPERS EN LA LISTA DE ARTEMIS")
    print("1.6 BUSCAR CAMPERS EN LA LISTA DE ARTEMIS POR EDAD")
    print("2.  CREAR GRUPO SPUTNIK")
    print("2.1 LISTAR CAMPERS DE SPUTNIK")
    print("2.2 AGREGAR CAMPERS A SPUTNIK")
    print("2.3 ELIMINAR CAMPERS A SPUTNIK")
    print("2.4 ORDENAR ALFABETICAMENTE EN LISTA DE SPUTNIK")
    print("2.5 BUSCAR CAMPERS EN LA LISTA DE SPUTNIK")
    print("2.6 BUSCAR CAMPERS EN LA LISTA DE SPUTNIK POR EDAD")
    op = float(input("Digite una opcion: "))
    if(op == 1 ):
        os.system("clear")
        artemis = []
        flagA = True
        print("grupo Artemis creado")
        print("presiona enter para continuar....\n")
        input("")
        os.system("clear")
    elif(op == 1.1):
        if(flagA == True):
            os.system("clear")
            print("***Lista Campers***")
            if(len(artemis)== 0):
                print("No hay campers en Artemis")
                print("presiona enter para continuar....\n")
                input("")
            else:
                os.system("clear")
                print(artemis)
                print("presiona enter para continuar....\n")
                input("")
        else:
            os.system("clear")
            print("Grupo Artemis No esta creado")
            print("presiona enter para continuar....\n")
            input("")
    elif(op == 1.2):
        if(flagA == True):
            os.system("clear")
            print("***Registro Camper***")
            nom = input("Ingresa nombre del camper: ")
            age = int(input("Ingresa la edad del camper: "))
            artemis.append([nom, age])
            print("presiona enter para continuar....\n")
            input("")
        else:
            os.system("clear")
            print("primero debes crear el grupo Artemis")
            print("presiona enter para continuar....\n")
            input("")
    elif(op == 1.3):
        if(flagA == True):
            os.system("clear")
            print("***Eliminar Camper***")
            nom = input("Ingresa nombre del camper a eliminar: ")
            for i in range(len(artemis)):
                if(artemis[i][0] == nom):
                    artemis.pop(i)
                    print("Camper eliminado")
                    print("presiona enter para continuar....\n")
                    input("")
                else:
                    print("El estudiante no se encuentra")
                    print("presiona enter para continuar....\n")
                    input("")
        else:
            os.system("clear")
            print("primero debes crear el grupo Artemis")
            print("presiona enter para continuar....\n")
            input("")
    elif(op == 1.4):
        if(flagA == True):
            os.system("clear")
            print("***Campers Alfabeticamente***")
            artemis1=[]
            for i in range(len(artemis)):
                artemis1.append(artemis[i][0])
            print(artemis1.sort())
            print("presiona enter para continuar....\n")
            input("")
        else:
            os.system("clear")
            print("primero debes crear el grupo Artemis")
            print("presiona enter para continuar....\n")
            input("")
    elif(op == 2 ):
        sputnik = []
