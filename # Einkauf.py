# Diese Funktion berechnet den Gesamtpreis für einen Einkauf unter Berücksichtigung von Rabatten.

# Die Aufgabenstellung lautet: 
# Schreibe ein Programm, das den Gesamtpreis für einen Einkauf berechnet.
# Der Benutzer soll die Anzahl der gekauften Artikel, den Preis pro Artikel und den Rabatt in Prozent eingeben.
# Das Programm soll dann den Gesamtpreis nach Abzug des Rabatts ausgeben.

# Benutzereingaben für Anzahl, Preis und Rabatt
anzahl = int(input("Eingabe Anzahl: "))
preis = int(input("Eingabe Preis: "))
rabatt = int(input("Eingabe Rabatt: "))

# Berechnung des normalen Preises ohne Rabatt
normal_preis = anzahl * preis

# Berechnung des Gesamtpreises nach Abzug des Rabatts
gesamt_preis = normal_preis - (normal_preis * rabatt/100)

# Ausgabe des Gesamtpreises
print(gesamt_preis)
