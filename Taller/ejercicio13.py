import os
os.system("cls")

num = int(input("Ingresa un numero: "))
for i in range(0,10):
    print(f"{num}*{i+1}={num*(i+1)}")