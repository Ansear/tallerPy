import os
os.system("cls")

cont = 0
acumulador = 1

while(cont < 50):
    if((acumulador%2)==0):
        print(acumulador)
        cont += 1
        acumulador += 1
    else:
        acumulador += 1    
