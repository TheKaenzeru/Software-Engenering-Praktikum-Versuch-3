import math
import json
with open("Labyrinth-1.txt", "r") as Labyrinth:
    LabHeight = 0
    LabLength = len(Labyrinth.readline()) - 1
    LabListeZeilen = []
    LabListeZeichen = []


    Labyrinth.seek(0)
    for line in Labyrinth:
        Zeile = line.rstrip()
        LabListeZeilen.append(list(Zeile))
        LabHeight+=1
    print(LabListeZeilen)
    print(LabHeight)
    print(LabLength)

    Labyrinth.close()