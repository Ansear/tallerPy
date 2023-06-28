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
    print("2.  CREAR GRUPO SPUTNIK")
    print("2.1 LISTAR CAMPERS DE SPUTNIK")
    print("2.2 AGREGAR CAMPERS A SPUTNIK")
    print("2.3 ELIMINAR CAMPERS A SPUTNIK")
    print("2.4 ORDENAR ALFABETICAMENTE EN LISTA DE SPUTNIK")
    print("2.5 BUSCAR CAMPERS EN LA LISTA DE SPUTNIK")
    print("3.SALIR.")
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
            if(nom == ""):
                print("por favor ingresa un dato valido")
                print("presiona enter para continuar....\n")
                input("")
            else:
                student = 0
                for i in range(len(artemis)):
                    artemis[i][0] == nom
                    if(artemis[i][0] == nom):
                        delete = True
                        student = i
                    else:
                        delete = False
                if(True):
                    artemis.pop(student)
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
        if((flagA == True) and (len(artemis)>=1)):
            os.system("clear")
            print("***Campers Alfabeticamente***")
            artemis1=[]
            for i in range(len(artemis)):
                artemis1.append(artemis[i][0])
            alfa = sorted(artemis1) 
            print(alfa)
            print("presiona enter para continuar....\n")
            input("")
        else:
            os.system("clear")
            print("primero debes crear el grupo Artemis")
            print("presiona enter para continuar....\n")
            input("")
    elif(op == 1.5):
        if(flagA == True):
            os.system("clear")
            print("***Buscar Camper***")
            nom = input("Ingresa nombre del camper a buscar: ")
            for i in range(len(artemis)):
                if(artemis[i][0] == nom):
                    search = True
                    student = artemis[i]
                    break
                else:
                    search = False
            if(search == True):
                print(f"estudiante: {student}")
                print("presiona enter para continuar....\n")
                input("")
            else:
                os.system("clear")
                print("El estudiante no se encuentra")
                print("presiona enter para continuar....\n")
                input("")
        else:
            os.system("clear")
            print("primero debes crear el grupo Artemis")
            print("presiona enter para continuar....\n")
            input("")
    if(op == 2 ):
        os.system("clear")
        sputnik = []
        flagS = True
        print("grupo Sputnik creado")
        print("presiona enter para continuar....\n")
        input("")
        os.system("clear")
    elif(op == 2.1):
        if(flagS == True):
            os.system("clear")
            print("***Lista Campers***")
            if(len(sputnik)== 0):
                print("No hay campers en Sputnik")
                print("presiona enter para continuar....\n")
                input("")
            else:
                os.system("clear")
                print(sputnik)
                print("presiona enter para continuar....\n")
                input("")
        else:
            os.system("clear")
            print("Grupo Sputnik No esta creado")
            print("presiona enter para continuar....\n")
            input("")
    elif(op == 2.2):
        if(flagS == True):
            os.system("clear")
            print("***Registro Camper***")
            nom = input("Ingresa nombre del camper: ")
            age = int(input("Ingresa la edad del camper: "))
            sputnik.append([nom, age])
            print("presiona enter para continuar....\n")
            input("")
        else:
            os.system("clear")
            print("primero debes crear el grupo Sputnik")
            print("presiona enter para continuar....\n")
            input("")
    elif(op == 2.3):
        if(flagS == True):
            os.system("clear")
            print("***Eliminar Camper***")
            nom = input("Ingresa nombre del camper a eliminar: ")
            if(nom == ""):
                print("Ingresa un valor valido")
                print("presiona enter para continuar....\n")
                input("")
            else:
                student = 0
                for i in range(len(sputnik)):
                    sputnik[i][0] == nom
                    if(sputnik[i][0] == nom):
                        delete = True
                        student = i
                    else:
                        delete = False
                if(True):
                    sputnik.pop(student)
                    print("Camper eliminado")
                    print("presiona enter para continuar....\n")
                    input("")
                else:
                    print("El estudiante no se encuentra")
                    print("presiona enter para continuar....\n")
                    input("")
        else:
            os.system("clear")
            print("primero debes crear el grupo Sputnik")
            print("presiona enter para continuar....\n")
            input("")
    elif(op == 2.4):
        if((flagS == True) and (len(sputnik)>=1)):
            os.system("clear")
            print("***Campers Alfabeticamente***")
            sputnik1=[]
            for i in range(len(sputnik)):
                sputnik1.append(sputnik[i][0])
            alfabeto = sorted(sputnik1) 
            print(alfabeto)
            print("presiona enter para continuar....\n")
            input("")
        else:
            os.system("clear")
            print("primero debes crear el grupo Sputnik")
            print("presiona enter para continuar....\n")
            input("")
    elif(op == 2.5):
        if(flagS == True):
            os.system("clear")
            print("***Buscar Camper***")
            nom = input("Ingresa nombre del camper a buscar: ")
            for i in range(len(sputnik)):
                if(sputnik[i][0] == nom):
                    search = True
                    student = sputnik[i]
                    break
                else:
                    search = False
            if(search == True):
                print(f"estudiante: {student}")
                print("presiona enter para continuar....\n")
                input("")
            else:
                os.system("clear")
                print("El estudiante no se encuentra")
                print("presiona enter para continuar....\n")
                input("")
        else:
            os.system("clear")
            print("primero debes crear el grupo Artemis")
            print("presiona enter para continuar....\n")
            input("")
    elif(op == 3):
        os.system("clear")
        print("Gracias por usar el programa....presiona enter para continuar\n")
        input("")
        flag = False