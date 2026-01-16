import math
import json
import os
print("Verfügbare Datein:")
LabAuswahlDatei = [f for f in os.listdir('.') if f.endswith(".txt") if f.startswith("Labyrinth")]
i = 0
for Lab in LabAuswahlDatei:
    i = i + 1
    print(i,":",Lab)
print("Wähle aus per Dateiname oder Nummer.")
LabDatei = input("Welchs Labyrinth soll geladen werden?: ")

if LabDatei.isdigit():
    LabDatei = LabAuswahlDatei[int(LabDatei)-1]

with open(LabDatei, "r") as Labyrinth:
    print("Du hast",LabDatei,"geladen.")
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
