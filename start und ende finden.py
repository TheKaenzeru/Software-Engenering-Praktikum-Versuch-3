import math
#amelie

def Start_und_ziel_f(Labyrinth, lab_height, lab_length):
    höhe= lab_height #Anzahl der "Zeilen" als Strings
    breite = lab_length #Anzahl der Elemente einer "Zeile"

    for i in range(höhe): ###Für jedes i einen schleifendurchlauf
        for j in range(breite): #Für jedes Element von i wird Schleife durchgeführt.
            if Labyrinth[i][j][1] == 'SX': #wenn X gefunden wird = start
                start = (i,j) #i,j werden "start" zugeordnet
            elif Labyrinth[i][j][1] == 'ZX': #Falls ein "Z" gefunden wird = ziel
                ziel = (i,j) #i,j werden "ziel" zugeordnet
            else:
                continue #Falls  kein zeichen: nächste Zeile absuchen
    return start, ziel #Wenn alle "Zeilen" durchgegangen sind, wird "start" und "ziel" zurückgegeben

#Labyrinth = kartendaten_normalisieren.Labyrinth # warum dort? Variable "Labyrinth" weisen wir die  neuen Daten

if __name__ == "__main__":
    from KartendatenNormaliesierne import normalisiere_karten_daten
    from DateiEinlesen import datei_auswahl, datei_einlesen

    lab_datei = datei_auswahl()
    lab_liste_zeilen, lab_height, lab_length, lab_wall = datei_einlesen(lab_datei)
    lab_normal, start_kord, ziel_kord, zahl_kord = normalisiere_karten_daten(lab_liste_zeilen, lab_wall, lab_height,
                                                                             lab_length)
    start_kord_amelie, ziel_kord_amelie = Start_und_ziel_f(lab_normal, lab_height, lab_length)

    print(start_kord_amelie, ziel_kord_amelie)
    print(start_kord, ziel_kord)
