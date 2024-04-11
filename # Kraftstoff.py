# Dieses Programm berechnet den Durchschnittsverbrauch an Kraftstoff pro 100 Kilometer.

# Die Aufgabenstellung lautet:
# Schreibe ein Programm, das den Durchschnittsverbrauch an Kraftstoff pro 100 Kilometer berechnet.
# Der Benutzer soll die Tankmenge in Litern und die zurückgelegte Strecke in Kilometern eingeben.
# Das Programm soll dann den Durchschnittsverbrauch in Litern pro 100 Kilometer ausgeben.

# Benutzereingabe für die Tankmenge in Litern
kraftstoff = int(input("Bitte geben Sie die Tankmenge in Litern an: "))

# Benutzereingabe für die zurückgelegte Strecke in Kilometern
gefahren = int(input("Bitte geben Sie die zurückgelegte Strecke in Kilometern an: "))

# Berechnung des Durchschnittsverbrauchs pro 100 Kilometer
gesamt = (kraftstoff * 100) / gefahren

# Ausgabe des Durchschnittsverbrauchs
print("Ihr Durchschnittsverbrauch (100 km) an Kraftstoff war:", gesamt)
