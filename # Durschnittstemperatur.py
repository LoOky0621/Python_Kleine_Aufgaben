# Aufgabenstellung: Durchschnittstemperatur aus CSV-Datei berechnen und ausgeben

import csv  # Importiere das csv-Modul zum Lesen von CSV-Dateien
import os   # Importiere das os-Modul zum Arbeiten mit Dateipfaden

summe = 0   # Initialisiere die Summe der Temperaturen

# Gib das aktuelle Arbeitsverzeichnis aus
print(os.getcwd())

# Wechsle das Arbeitsverzeichnis zu "c:/Users/Student/Desktop/Übungen Python GFN"
os.chdir("c:/Users/Student/Desktop/Übungen Python GFN")

# Gib das aktualisierte Arbeitsverzeichnis aus
print(os.getcwd())

# Öffne die CSV-Datei "temp.csv" im Lese-Modus
with open("temp.csv") as csvdatei:
    
    # Erzeuge ein CSV-Leser-Objekt
    csvdaten_objekt = csv.reader(csvdatei, delimiter=",")
    
    # Konvertiere das CSV-Leser-Objekt in eine Liste von Listen
    temperaturen_liste = list(csvdaten_objekt)
    
    # Gib das CSV-Leser-Objekt aus
    print(csvdaten_objekt)

# Iteriere über jede Zeile der Liste und summiere die Temperaturen
for i in range(0, len(temperaturen_liste)):
    summe += float(temperaturen_liste[i][0])

# Iteriere über jede Zeile der Liste und gib die Temperaturen aus
for i in range(0, len(temperaturen_liste)):
    print("Temperatur", i + 1, "ist", temperaturen_liste[i][0], "°C")

# Berechne den Durchschnitt der Temperaturen
durchschnitt = summe / len(temperaturen_liste)

# Gib den Durchschnitt der Temperaturen aus
print("Der Durchschnitt der Temperaturen beträgt:", round(durchschnitt, 1), "°C")
