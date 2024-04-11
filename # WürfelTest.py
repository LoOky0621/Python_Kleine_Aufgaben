import random  # Importiere die random-Bibliothek für die Generierung von Zufallszahlen

# Aufgabenstellung: Würfel-Simulation
# Schreibe ein Programm, das eine Simulation für das Werfen eines Würfels durchführt.
# Das Programm soll eine zufällige Zahl zwischen 1 und 6 generieren und diese ausgeben.
# Die Simulation soll solange fortgesetzt werden, bis die generierte Zahl die 6 ist.
# Die Anzahl der Würfe soll ebenfalls ausgegeben werden.

# Initialisiere eine Zählvariable für die Anzahl der Würfe
anzahl_würfe = 0

# Führe eine Schleife aus, bis eine 6 gewürfelt wird
while True:
    # Generiere eine zufällige Zahl zwischen 1 und 6
    wurf = random.randint(1, 6)
    
    # Inkrementiere die Zählvariable für die Anzahl der Würfe
    anzahl_würfe += 1
    
    # Gib die gewürfelte Zahl aus
    print("Wurf", anzahl_würfe, ":", wurf)
    
    # Überprüfe, ob eine 6 gewürfelt wurde
    if wurf == 6:
        # Wenn eine 6 gewürfelt wurde, beende die Schleife
        break

# Gib die Anzahl der insgesamt durchgeführten Würfe aus
print("Es wurden insgesamt", anzahl_würfe, "Würfe benötigt, um eine 6 zu würfeln.")
