# Aufgabenstellung: Berechnung einer Summe unter Berücksichtigung von Bedingungen
# Schreibe ein Programm, das eine Schleife verwendet, um eine Summe zu berechnen.
# Die Summe soll unter Berücksichtigung bestimmter Bedingungen erfolgen.
# Das Programm soll die folgenden Operationen durchführen:
# 1. Eine Variable i wird mit dem Wert 10 initialisiert.
# 2. Eine Variable z wird mit dem Wert 100 initialisiert.
# 3. Eine Schleife wird so lange durchlaufen, wie i größer als 0 ist.
# 4. In jedem Schleifendurchlauf wird überprüft, ob i gerade ist (durch 2 teilbar).
#    - Wenn i gerade ist, wird i von z subtrahiert.
#    - Wenn i ungerade ist, wird i zu z addiert.
# 5. Der Wert von i wird um 1 reduziert.

# Initialisierung der Variablen
i = 10
z = 100

# Schleife läuft, solange i größer als 0 ist
while i > 0:
    # Überprüfen, ob i gerade ist
    if i % 2 == 0:
        # Wenn i gerade ist, wird i von z subtrahiert
        z = z - i
    else:
        # Wenn i ungerade ist, wird i zu z addiert
        z = z + i
    # i um 1 reduzieren
    i = i - 1

# Ausgabe des finalen Wertes von z
print(z)
