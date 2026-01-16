from DateiEinlesen import Labyrinth, LabListeZeilen, LabWall, LabHeight, LabLength
LabNormal = []
StartKord = []
ZielKord = []
ZahlKord = []
i = 0
while i < LabHeight:
    LabZeichen = []
    j = 0
    while j < LabLength:

        if LabListeZeilen[i][j] == "W" and LabWall == "W":
            LabZeichen.append(["WX",0,0])
        elif LabListeZeilen[i][j] == "X":
            LabZeichen.append(["WX",0,0])

        elif LabListeZeilen[i][j] == "W" and LabWall == "X":
            LabZeichen.append(["GX",0,0])
        elif LabListeZeilen[i][j] == ".":
            LabZeichen.append(["GX",0,0])
        elif LabListeZeilen[i][j].isdigit():
            LabZeichen.append(["GX",0,LabListeZeilen[i][j]])
            ZahlKord.append([LabListeZeilen[i][j],i,j])

        elif LabListeZeilen[i][j] == "S":
            LabZeichen.append(["SX",1,0])
            StartKord =[i,j]
        elif LabListeZeilen[i][j] == "Z":
            LabZeichen.append(["ZX",0,0])
            ZielKord = [i,j]
        j = j + 1
    LabNormal.append(LabZeichen)
    i = i + 1


print(LabListeZeilen)
print(LabNormal)
print()
print("StartKordinaten bei:" ,StartKord)
print("ZielKordinaten bei:" ,ZielKord)
print("Zahl Kordinaten bei ",ZahlKord)

print(LabNormal[LabHeight-1][LabLength-1][0])