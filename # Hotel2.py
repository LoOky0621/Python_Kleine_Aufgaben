# Aufgabenstellung: Hoteloptionen anzeigen
#
# Entwickle ein Python-Programm, das basierend auf den Eingaben des Benutzers die verfügbaren Hoteloptionen ausgibt. Das Programm soll den Benutzer nach seinen Präferenzen für verschiedene Hotelangebote fragen und dann die entsprechenden Optionen anzeigen.
#
# Das Programm soll folgende Funktionen haben:
# 1. Fordere den Benutzer auf, folgende Informationen einzugeben:
#    - Möchte der Benutzer das Wellness-Komplettpaket? (1 für Ja, 0 für Nein)
#    - Möchte der Benutzer mehr als 3 Übernachtungen buchen? (1 für Ja, 0 für Nein)
#    - Möchte der Benutzer Vollpension? (1 für Ja, 0 für Nein)
#
# 2. Basierend auf den Benutzereingaben soll das Programm die ausgewählten Optionen anzeigen und die verfügbaren Leistungen auflisten.
#
# Das Programm soll folgende Leistungen für die ausgewählten Optionen anzeigen:
# - Frühstück + Abendbrot
# - Mittagessen
# - Fünf Freigetränke
# - Freie Nutzung des Fitnessraums
# - Saunabesuch gratis
# - Eine Massage gratis
#
# Das Programm soll dem Benutzer klare Anweisungen geben und die Ergebnisse übersichtlich präsentieren.

# Definition der Optionen
wel = "Wellness-Komplettpaket"
ab3 = "drei Übernachtungen"
voll = "Vollpension"

# Eingabeaufforderungen für den Benutzer
print("Bitte geben Sie 1 für Wellness-Komplettpaket ein, ansonsten 0")
w = input()
print("Bitte geben Sie 1 für mehr als 3 Übernachtungen ein, ansonsten 0")
ab = input()
print("Bitte geben Sie 1 für Vollpension ein, ansonsten 0")
v = input()

# Abfrage für das Wellness-Komplettpaket
if w == "1":
    print("Sie haben das:", wel)
    w = 1
else:
    print("Kein:", wel)
    w = 0

# Abfrage für mehr als 3 Übernachtungen
if ab == "1":
    print("Sie haben:", ab3)
    ab = 1
else:
    print("Keine:", ab3)  
    ab = 0 

# Abfrage für Vollpension
if v == "1":
    print("Sie haben:", voll)
    v = 1
else:
    print("Keine:", voll)
    v = 0

# Optionen für die Ausgabe
früh = "Frühstück + Abendbrot" 
mitt = "Mittagessen"        
fünf = "Fünf Freigetränke"
frei = "Freie Nutzung des Fitnessraums"
sau = "Saunabesuch gratis"
ein = "Eine Massage gratis"

# Verzweigung basierend auf den Eingaben des Benutzers
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
