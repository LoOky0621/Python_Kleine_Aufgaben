# Aufgabenstellung: Durchschnittstemperatur von zufälligen Temperaturen berechnen

import random  # Importiere das random-Modul zum Generieren von Zufallszahlen

# Generiere eine zufällige Anzahl von Temperaturen zwischen 2 und 10
anzahl = random.randint(2, 10)

i = 0  # Initialisiere den Zähler für die Schleife
summe = 0  # Initialisiere die Summe der Temperaturen
temperaturen = []  # Initialisiere eine leere Liste für die Temperaturen

# Schleife zur Generierung und Berechnung von Temperaturen
while i < anzahl:
    zufall = random.randint(1, 20)  # Generiere eine Zufallstemperatur zwischen 1 und 20
    temperaturen.append(zufall)  # Füge die Zufallstemperatur der Liste hinzu
    summe = summe + temperaturen[i]  # Addiere die Temperatur zur Gesamtsumme
    print("Die {0}. Temperatur in °C ist: ".format(i + 1), zufall)  # Gib die Zufallstemperatur aus
    i = i + 1  # Inkrementiere den Zähler für die Schleife

# Berechne den Durchschnitt der Temperaturen
durchschnitt = summe / anzahl

# Gib den Durchschnitt der Temperaturen aus
print("Die Durchschnittstemperatur beträgt: ", durchschnitt)
