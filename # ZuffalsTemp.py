# Aufgabenstellung: Zufällige Temperaturen generieren und Durchschnitt berechnen

import random  # Importiere das random-Modul für die Zufallsgenerierung

random.seed()  # Setze den Zufallsgenerator auf einen zufälligen Startwert

anzahl = 100  # Anzahl der zu generierenden Temperaturen
i = 0         # Initialisiere den Zähler für die Schleife
summe = 0     # Initialisiere die Summe der Temperaturen
temperaturen = []  # Initialisiere eine leere Liste für die Temperaturen

# Schleife zur Generierung und Berechnung von Temperaturen
while i < anzahl:
    zufall = random.randint(5, 30)  # Generiere eine Zufallstemperatur zwischen 5 und 30
    print("Die {0}. Temperatur in °C ist: ".format(i + 1), zufall)  # Gib die Zufallstemperatur aus
    temperaturen.append(zufall)  # Füge die Zufallstemperatur der Liste hinzu
    summe = summe + temperaturen[i]  # Addiere die Temperatur zur Gesamtsumme
    i = i + 1  # Inkrementiere den Zähler für die Schleife

# Berechne den Durchschnitt der Temperaturen
durchschnitt = summe / anzahl

# Gib den Durchschnitt der Temperaturen aus
print("Die Durchschnittstemperatur beträgt: ", durchschnitt)
