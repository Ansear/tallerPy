import os 
import equipos 

if __name__ == '__main__':
    teams = []
    isAddTeam = True
    opcion = 0
    while isAddTeam:
        os.system("clear")
        print("1.Registrar equipo\n2.Mostrar equipos\n3.Registrar Jugador\n4.Registrar Cuerpo Tecnico\n5.Registrar Cuerpo Medico\n6.Mostrar Entrenadores")
        try:
            opcion = int(input(":)"))
            if (opcion == 1):
                equipos.AddEquipo(teams)
            elif(opcion == 2):
                os.system("clear")
                print(teams)
                print("Presiona enter para continuar...\n")
                input("..")
            elif(opcion == 3):
                os.system("clear")
                equipos.AddPlayer(teams)
                print("Presiona enter para continuar...\n")
                input("..")
            elif(opcion == 4):
                os.system("clear")
                equipos.AddTecnico(teams)
                print("Presiona enter para continuar...\n")
                input("..")
            elif(opcion == 5):
                os.system("clear")
                equipos.AddMedico(teams)
                print("Presiona enter para continuar...\n")
                input("..")
            elif(opcion == 6):
                os.system("clear")
                equipos.ShowTrainer(teams)
                print("Presiona enter para continuar...\n")
                input("..")
        except ValueError:
            print("No se reconoce el tipo de dato del valor ingresado")
            print("Presiona enter para continuar...\n")
            input("..")
        else:
            isAddTeam = bool(input("Desea continuar en el programa S(si) o Enter(No): "))