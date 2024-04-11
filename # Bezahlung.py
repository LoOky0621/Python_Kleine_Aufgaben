# Aufgabenstellung: Bezahlungsoptionen
# Entwickle ein Programm, das basierend auf verschiedenen Bedingungen die verfügbaren Zahlungsmöglichkeiten für Kunden anzeigt.
# Die Bedingungen beziehen sich auf das Land des Kunden, die Akzeptanz von Kreditkarten und ob der Kunde ein Neukunde ist.
# Das Programm soll die folgenden Bedingungen abfragen:
# 1. Gibt der Kunde an, dass er aus dem Ausland kommt?
# 2. Akzeptiert das Geschäft Kreditkarten?
# 3. Ist der Kunde ein Neukunde?
# Basierend auf den Antworten des Kunden sollen verschiedene Zahlungsoptionen angezeigt werden.

# Bedingungen definieren
aus = "Ausland"
krea = "Kreditkarte Akzeptiert"
neu = "Neukunde"

# Benutzer nach den Bedingungen fragen und die Antworten speichern
print("Bitte geben Sie 1 für", aus, "ein, ansonsten 0:")
a = input()
print("Bitte geben Sie 1 für", krea, "ein, ansonsten 0:")
k = input()
print("Bitte geben Sie 1 für", neu, "ein, ansonsten 0:")
n = input()

# Abfrage für die erste Bedingung: Ausland
if a == "1":
    print(aus)
    a = 1
else:
    print("Kein:", aus)
    a = 0

# Abfrage für die zweite Bedingung: Kreditkartenakzeptanz
if k == "1":
    print(krea)
    k = 1
else:
    print("Keine:", krea)
    k = 0 

# Abfrage für die dritte Bedingung: Neukunde
if n == "1":
    print(neu)
    n = 1
else:
    print("Kein:", neu)
    n = 0

# Variablen für die Ausgabe der Zahlungsmöglichkeiten
last = "Lastschriftverfahren"
vor = "Vorkasse"
kre = "Kreditkarte"

# Verzweigung basierend auf den Bedingungen, um die verfügbaren Zahlungsmöglichkeiten anzuzeigen
if a == 1 and k == 1 and n == 1:
    print("Sie können die folgenden Zahlungsmöglichkeiten benutzen:", kre)
elif a == 1 and k == 1 and n == 0:
    print("Sie können die folgenden Zahlungsmöglichkeiten benutzen:", kre)
elif a == 1 and k == 0 and n == 1:
    print("Sie können die folgenden Zahlungsmöglichkeiten benutzen:", vor)    
elif a == 1 and k == 0 and n == 0:
    print("Sie können die folgenden Zahlungsmöglichkeiten benutzen:", vor)                    
elif a == 0 and k == 1 and n == 1:
    print("Sie können die folgenden Zahlungsmöglichkeiten benutzen:", kre, vor)
elif a == 0 and k == 1 and n == 0:
    print("Sie können die folgenden Zahlungsmöglichkeiten benutzen:", kre, vor, last)
elif a == 0 and k == 0 and n == 1:
    print("Sie können die folgenden Zahlungsmöglichkeiten benutzen:", vor)
elif a == 0 and k == 0 and n == 0:
    print("Sie können die folgenden Zahlungsmöglichkeiten benutzen:", vor, last)
