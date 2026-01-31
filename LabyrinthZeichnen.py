#amelie

import datei_einlesen
import gfx_stack as gfx
import kartendaten_normalisieren



def Spielfeld_Zeichnen(Labyrinth):
    höhe = len(Labyrinth) #Höhe ist die Länge der Liste, also die Anzahl der Strings
    breite = len(Labyrinth[0]) #Breite ist die Länge von jedem String

    gfx.init_once((breite, höhe)) #gibt das Ausgabefeld aus
    for i in range(höhe):#kontrolliert jede Zeile
        for j in range (breite):#kontrolliert jedes Element in der Zeile

            if Labyrinth[i][j] == '.':  #Punkt ist Weg
                gfx.set_pixel((j,i),'Elf Green') # der noch nicht gegangene Weg ist türkis

            elif Labyrinth[i][j] == 'WX': #W ist Wand
                gfx.set_pixel((j,i),'Black')# schwarz ist die farbe der wände

            elif Labyrinth[i][j] == 'SX': #S ist Start
                gfx.set_pixel((j, i), 'Atlantis')#start ist balu

            elif Labyrinth[i][j] == 'ZX': #ZX ist Ziel
                gfx.set_pixel((j, i),"Christi" ) #ziel ist grün

            else: #alles andere, Bonusaufgaben
                gfx.set_pixel((j, i), "Mandy" ) # hellrot dür die zuastzpunkte

Labyrinth = kartendaten_normalisieren.normierung(datei_einlesen.Öffnen()) #Müssen sagen welches Labyrinth er benutzen soll,  eingabe bereits in Karte einlesen erfolgt
Spielfeld_Zeichnen(Labyrinth) #Programm wird einmal ausgeführt
while not gfx.stop_prog: #solange das Programm nicht beendet werden soll
    gfx.event_loop()# weitere eingaben können verarbeitet werden