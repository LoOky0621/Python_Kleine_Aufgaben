# Dieses Programm simuliert eine Hotelbuchung mit verschiedenen Optionen.

# Die Aufgabenstellung lautet:
# Schreibe ein Programm, das die Buchungsoptionen für ein Hotel simuliert.
# Der Benutzer soll auswählen können, ob er das Wellness-Komplettpaket, mehr als drei Übernachtungen und Vollpension möchte.
# Basierend auf den Auswahlmöglichkeiten soll das Programm die verfügbaren Leistungen ausgeben.

# Definition der Bedingungen für die Buchungsoptionen
wel = "Wellness-Komplettpaket"
ab3 = "drei Übernachtungen"
voll = "Vollpension"

# Benutzereingaben für die Buchungsoptionen
print("Bitte geben Sie 1 für Wellness-Komplettpaket ein, ansonsten 0:")
w = input()
print("Bitte geben Sie 1 für mehr als drei Übernachtungen ein, ansonsten 0:")
ab = input()
print("Bitte geben Sie 1 für Vollpension ein, ansonsten 0:")
v = input()

# Verarbeitung der Benutzereingaben und Ausgabe der ausgewählten Buchungsoptionen
if w == "1":
    print("Sie haben das:", wel)
    w = 1
else:
    print("Kein:", wel)
    w = 0

if ab == "1":
    print("Sie haben:", ab3)
    ab = 1
else:
    print("Keine:", ab3)  
    ab = 0 

if v == "1":
    print("Sie haben:", voll)
    v = 1
else:
    print("Keine:", voll)
    v = 0

# Definition der verfügbaren Leistungen
früh = "Frühstück + Abendbrot" 
mitt = "Mittagessen"        
fünf = "Fünf Freigetränke"
frei = "Freie Nutzung des Fitnessraums"
sau = "Saunabesuch gratis"
ein = "Eine Massage gratis"

# Verzweigung basierend auf den ausgewählten Buchungsoptionen
if w == 1 and ab == 1 and v == 1:
    print("Sie verfügen über:", früh, ",", mitt, ",", fünf, ",", frei, ",", sau, ",", ein)
elif w == 1 and ab == 1 and v == 0:
    print("Sie verfügen über:", früh, ",", fünf, ",", frei, ",", sau, ",", ein)
elif w == 1 and ab == 0 and v == 1:
    print("Sie verfügen über:", früh, ",", mitt, ",", fünf, ",", frei, ",", sau, ",", ein)
elif w == 1 and ab == 0 and v == 0:
    print("Sie verfügen über:", früh, ",", fünf, ",", frei, ",", sau, ",", ein)
elif w == 0 and ab == 1 and v == 1:
    print("Sie verfügen über:", früh, ",", mitt, ",", fünf, ",", frei, ",", sau)
elif w == 0 and ab == 1 and v == 0:
    print("Sie verfügen über:", früh, ",", frei, ",", sau)
elif w == 0 and ab == 0 and v == 1:
    print("Sie verfügen über:", früh, ",", mitt, ",", fünf, ",", frei)
elif w == 0 and ab == 0 and v == 0:
    print("Sie verfügen über:", früh, ",", frei)                        
