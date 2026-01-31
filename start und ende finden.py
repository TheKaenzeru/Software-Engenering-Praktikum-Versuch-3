import math
#amelie

import kartendaten_normalisieren

def Start_und_ziel_f(Labyrinth):
    höhe = len(Labyrinth) #Anzahl der "Zeilen" als Strings
    breite = len(Labyrinth[0]) #Anzahl der Elemente einer "Zeile"

    for i in range(höhe): ###Für jedes i einen schleifendurchlauf
        for j in range(breite): #Für jedes Element von i wird Schleife durchgeführt.
            if Labyrinth[i][j] == 'SX': #wenn X gefunden wird = start
                start = (i,j) #i,j werden "start" zugeordnet
            elif Labyrinth[i][j] == 'ZX': #Falls ein "Z" gefunden wird = ziel
                ziel = (i,j) #i,j werden "ziel" zugeordnet
            else:
                continue #Falls  kein zeichen: nächste Zeile absuchen

    return start,ziel #Wenn alle "Zeilen" durchgegangen sind, wird "start" und "ziel" zurückgegeben

Labyrinth = kartendaten_normalisieren.Labyrinth # warum dort? Variable "Labyrinth" weisen wir die  neuen Daten