import os

def datei_auswahl(): ## hier wird in die konsole alle im datei Pfad hinterlegten Labyrint Datein ausgegeben die Gefunden werden und man muss das Labyrint auswählen das durchlaufen werden soll
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
    return LabDatei ## die Ausgabe ist die Lab datei. Diese wir nur für die nächste Funktion benötigt

def datei_einlesen(LabDatei): ## hier wird jetzt die grade rrausgesuchte Datei durhcgegangen und alles in eine 2D Liste geschrieben
    with open(LabDatei, "r") as Labyrinth:
        print("Du hast",LabDatei,"geladen.")
        LabHeight = 0
        LabLength = len(Labyrinth.readline()) - 1
        Labyrinth.readline()
        Labyrinth.readline()
        if Labyrinth.read(1) == "W":
            LabWall = "W"
        else:
            LabWall = "X"

        Labyrinth.seek(0)
        LabListeZeilen = []
        for line in Labyrinth:
            Zeile = line.rstrip()
            LabListeZeilen.append(list(Zeile))
            LabHeight+=1
    return LabListeZeilen, LabHeight, LabLength, LabWall ## hier werden die Liste des labyrints, wie groß es ist und ob die wand W oder X sind ausgegeben

#if __name__ == "__main__": #fürs debugging
    LabDatei = datei_auswahl()
    LabListeZeilen, LabHeight, LabLength, LabWall = datei_einlesen(LabDatei)
    #print(LabListeZeilen)
    #print(LabHeight)
    #print(LabLength)
    #print(LabWall)
