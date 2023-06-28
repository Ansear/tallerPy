import os
os.system("cls")

word = input("Ingresa una frase: ")
cont = 0
for i in range(len(word)):
    if (word[i] == "a"):
        cont+=1
print(f"La letra 'a' esta {cont} veces en la frase: {word}")