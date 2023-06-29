import os 
def AddEquipo(equipos):
    os.system("clear")
    teamName = input("Ingrese el nombre del equipo: ").upper()
    myTeam = [teamName,[],[],[],[]]
    equipos.append(myTeam)

def AddPlayer(equipos):
    isAddPlayer = True
    equipo = input("Ingrese el nombre del equipo: ").upper()
    for item in equipos:
        if equipo in item:
            while isAddPlayer:
                posiciones = ["Arquero","Defensa","Delantero","Medio Central"]
                nombrePlayer = input("Ingrese el nombre del player: ")
                edadPlayer = int(input("Ingrese la edad del player: "))
                dorsalPlayer = int(input("Ingrese el dorsal del player: "))
                print("Seleccione la posicion del jugador: ")
                for i,pos in enumerate(posiciones):
                    print(f"{i+1}. {pos}")
                posicionPlayer = posiciones[int(input())-1]
                jugador=[nombrePlayer,edadPlayer,posicionPlayer,dorsalPlayer]
                item[1].append(jugador)
                isAddPlayer = bool(input("Desea agregar otro jugador S(Si) Enter(No): "))

def AddTecnico(equipos):
    isAddTecnico = True
    equipo = input("Ingrese el nombre del equipo: ").upper()
    for item in equipos:
        if equipo in item:
            while isAddTecnico:
                cargos = ["Asistente Tecnico","Tecnico","Director Tecnico","Entrenador"]
                nombreTecnico = input("Ingrese el nombre del Tecnico: ")
                edadTecnico = int(input("Ingrese la edad del Tecnico: "))
                print("Seleccione la posicion del Tecnico: ")
                for i,car in enumerate(cargos):
                    print(f"{i+1}. {car}")
                cargoTecnico = cargos[int(input())-1]
                tecnico=[nombreTecnico,edadTecnico,cargoTecnico]
                item[2].append(tecnico)
                isAddTecnico = bool(input("Desea agregar otra persona al cuerpo tecnico S(Si) Enter(No): "))

def AddMedico(equipos):
    isAddMedico = True
    equipo = input("Ingrese el nombre del equipo: ").upper()
    for item in equipos:
        if equipo in item:
            while isAddMedico:
                cargos = ["Psicológo","Fisioterapeuta","Camillero","Masajista"]
                nombreMedico = input("Ingrese el nombre del Médico: ")
                edadMedico = int(input("Ingrese la edad del Médico: "))
                print("Seleccione la posicion del médico: ")
                for i,car in enumerate(cargos):
                    print(f"{i+1}. {car}")
                cargoMedico = cargos[int(input())-1]
                medico=[nombreMedico,edadMedico,cargoMedico]
                item[3].append(medico)
                isAddMedico = bool(input("Desea agregar otra persona al cuerpo tecnico S(Si) Enter(No): "))
def ShowTrainer(equipos):
    
    for equipo in (equipos):
        for tec in (equipos[2]):
            if "Director tecnico" in tec:
                print("|{:^15}{}{:^20}|.format('')")
            # if(equipos[i][2][i][2] == "Entrenador"):
            #     print()
            #     print(f"Pais:{equipos[i][0]}, Entrenador:{equipos[i][2][i][0]}")
            # else:
            #     print(f"El pais:{equipos[i][0]} no tiene entrenador")

