from DateiEinlesen import datei_auswahl, datei_einlesen
from KartendatenNormaliesierne import normalisiere_karten_daten

def main():
    # 1. Datei auswählen
    lab_datei = datei_auswahl()
    # 2. Datei einlesen
    lab_liste_zeilen, lab_height, lab_length, lab_wall = datei_einlesen(lab_datei) #benutz die datei aus dem schrit oben drüber
    # 3. Daten normalisieren
    lab_normal, start_kord, ziel_kord, zahl_kord = normalisiere_karten_daten(lab_liste_zeilen, lab_wall, lab_height, lab_length) #benutz die variablen aus dem schritt oben drüber
    #alle diese Variablen können jetz weiter benutzt werden
    #das normaliesierte Labyritn ist in "lab_normal" gespeichert
    #alle ausgaben von koordinaten sind die richtigen kordinaten für die Listen also können direkt zum suchen übernommen werden.
    #   Im echten labyrint ist es natürlich +1 in jede richtung da listen ja bei null anfangen zu zählen

    print("\n--- Ergebnisse im Main-Programm ---")
    print(f"Geladenes Labyrinth: {lab_datei}")
    print(f"Startpunkt: {start_kord}")
    print(f"Zielpunkt: {ziel_kord}")
    print(lab_normal)

main()
