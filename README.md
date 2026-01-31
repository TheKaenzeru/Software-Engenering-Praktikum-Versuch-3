# Software-Engenering-Praktikum-Versuch-3
Die Funktionen der Datei einlese können per:  

    from DateiEinlesen import datei_auswahl, datei_einlesen 
importiert werden und mit:  

		lab_datei = datei_auswahl() 
und:  

  	lab_liste_zeilen, lab_height, lab_length, lab_wall = datei_einlesen(lab_datei) 
genutze werden 

Für die Funktion der Labyrithn normaliesierung gilt das gleiche:  

    from KartendatenNormaliesierne import normalisiere_karten_daten 
bei den Funtktionen muss draucf geachtet werden das an die Funktion die werde aus der Datei einlese übergeben werden müssen also entsprechend:

    from DateiEinlesen import datei_auswahl, datei_einlesen 
    lab_datei = datei_auswahl() 
    lab_liste_zeilen, lab_height, lab_length, lab_wall = datei_einlesen(lab_datei) 
    lab_normal, start_kord, ziel_kord, zahl_kord = normalisiere_karten_daten(lab_liste_zeilen, lab_wall, lab_height, lab_length) 
