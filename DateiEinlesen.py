import math
import json
with open("Labyrinth-3.txt", "r") as Labyrinth:
    LabHeight = 0
    LabLength = len(Labyrinth.readline()) - 1
    LabWall = ""
    LabListeZeilen = []
    LabListeZeichen = []
    Labyrinth.readline()
    Labyrinth.readline()
    if Labyrinth.read(1) == "W":
        LabWall = "W"
    else:
        LabWall = "X"

    Labyrinth.seek(0)
    for line in Labyrinth:
        Zeile = line.rstrip()
        LabListeZeilen.append(list(Zeile))
        LabHeight+=1
    print(LabListeZeilen)
    print(LabHeight)
    print(LabLength)
    print(LabWall)

    Labyrinth.close()