# Aufgabenstellung: Berechnung einer komplexen Operation
# Schreibe ein Programm, das eine komplexe Berechnung in einer Schleife durchführt und das Ergebnis ausgibt.
# Das Programm soll die folgende Operation ausführen:
# 1. Eine Variable z wird mit dem Wert 4 initialisiert.
# 2. Eine Variable i wird mit dem Wert 4 initialisiert.
# 3. Eine Schleife wird so lange durchlaufen, wie i größer als 0 ist.
# 4. In jedem Schleifendurchlauf wird z um 4 erhöht und dann durch i geteilt.
# 5. Der Wert von i wird um 1 reduziert.

# Initialisierung der Variablen
z = 4
i = 4

# Schleife läuft, solange i größer als 0 ist
while i > 0:
    # z um 4 erhöhen
    z = z + 4
    # z durch i teilen
    z = z / i
    # i um 1 reduzieren
    i = i - 1

# Ausgabe des finalen Wertes von z
print(z)
