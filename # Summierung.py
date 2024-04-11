# Aufgabenstellung: Summierung in einer verschachtelten Schleife
# Schreibe ein Programm, das eine verschachtelte Schleife verwendet, um die Summe von Zahlen zu berechnen.
# Das Programm soll die Summe der Zahlen von 0 bis 19 (einschließlich) in 5er-Schritten berechnen.

# Initialisierung der Variablen für die Summe (z) und den äußeren Zähler (i)
i = 0
z = 0

# Äußere Schleife läuft, solange i kleiner als 20 ist, in 5er-Schritten
while i < 20:
    # Innerer Zähler (j) wird auf den Wert von i gesetzt
    j = i
    # Innere Schleife läuft, solange j kleiner als 20 ist
    while j < 20:
        # Addiere j zur Summe (z) hinzu
        z = z + j
        # Inkrementiere j
        j = j + 1
    # Inkrementiere i um 5 für den nächsten Durchlauf der äußeren Schleife
    i = i + 5

# Ausgabe der berechneten Summe
print(z)
