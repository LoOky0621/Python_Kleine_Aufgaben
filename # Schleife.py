# Aufgabenstellung: Benutzereingabe mit Schleifenbedingung
# Schreibe ein Programm, das den Benutzer nach einer Eingabe fragt und diese Eingabe überprüft.
# Die Schleife soll so lange laufen, bis der Benutzer entweder die Zahl 1 oder die Zahl 2 eingibt.

# Initialisierung der Variable für die Benutzereingabe
z = 0

# Schleife läuft, solange die Benutzereingabe weder 1 noch 2 ist
while z != 1 or z != 2:
    # Benutzer nach einer Eingabe fragen und den Wert in z speichern
    z = input()

# Ausgabe der finalen Benutzereingabe
print(z)
