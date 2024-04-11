# Diese Funktion berechnet die Fakultät einer gegebenen Zahl.

# Die Aufgabenstellung lautet:
# Schreibe ein Programm, das die Fakultät einer gegebenen Zahl berechnet.
# Der Benutzer soll eine Zahl eingeben.
# Das Programm soll dann die Fakultät dieser Zahl berechnen und ausgeben.

# Benutzereingabe für die Zahl, deren Fakultät berechnet werden soll
zahl = int(input("Bitte geben Sie eine Zahl ein: "))

# Initialisierung der Variablen für die Schleife
i = 1
zahlneu = 1

# Schleife zur Berechnung der Fakultät
while i <= zahl:
    zahlneu = i * zahlneu
    i += 1

# Ausgabe der berechneten Fakultät
print(zahlneu)
